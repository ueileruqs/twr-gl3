import streamlit as st
import json
import os
from alimentos_dados import dados

ARQUIVO_REFEICOES = "refeicoes_salvas.json"

def carregar_refeicoes_salvas():
    if os.path.exists(ARQUIVO_REFEICOES):
        with open(ARQUIVO_REFEICOES, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def salvar_refeicao_no_disco(nome, itens):
    ref_salvas = carregar_refeicoes_salvas()
    ref_salvas[nome] = itens
    with open(ARQUIVO_REFEICOES, "w", encoding="utf-8") as f:
        json.dump(ref_salvas, f, indent=4, ensure_ascii=False)
    return ref_salvas
    
def remover_refeicao_do_disco(nome):
    ref_salvas = carregar_refeicoes_salvas()
    if nome in ref_salvas:
        del ref_salvas[nome]
        with open(ARQUIVO_REFEICOES, "w", encoding="utf-8") as f:
            json.dump(ref_salvas, f, indent=4, ensure_ascii=False)
    return ref_salvas

# Transforma a base para o formato do app com Índice Glicêmico e Carga Glicêmica
alimentos_db = {}
for categoria, itens in dados.items():
    alimentos_db[categoria] = {}
    for nome, valores in itens.items():
        alimentos_db[categoria][nome] = {
            "cal": valores[0],
            "carb": valores[1],
            "prot": valores[2],
            "fat": valores[3],
            "medidas": valores[4],
            "ig": valores[5] if len(valores) > 5 else 0
        }

st.set_page_config(page_title="Calculadora Diabética", page_icon="🩸", layout="centered")

# Customização via CSS para melhor UI
st.markdown("""
    <style>
    div[data-testid="metric-container"] {
        background-color: #f7f9fa;
        border: 1px solid #e1e4e8;
        padding: 5% 5% 5% 10%;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    .ig-baixo { color: #28a745; font-weight: bold; }
    .ig-medio { color: #ffc107; font-weight: bold; }
    .ig-alto { color: #dc3545; font-weight: bold; }
    .insulin-box { 
        background-color: #e3f2fd; 
        border: 2px solid #2196f3; 
        border-radius: 8px; 
        padding: 15px; 
        margin-top: 20px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🩸 Macros & Insulina (NovoRapid)")
st.markdown("Acompanhe Calorias, **Carboidratos**, **Índice Glicêmico** e estime sua dose de insulina basal/bolus.")

# Estado global da sessão
if 'refeicao' not in st.session_state:
    st.session_state.refeicao = []

if 'refeicoes_salvas_db' not in st.session_state:
    st.session_state.refeicoes_salvas_db = carregar_refeicoes_salvas()

# =======================
# SIDEBAR
# =======================
with st.sidebar:
    st.header("⚙️ Configuração (DM)")
    # Fator de Carboidrato do usuário (Quantos gramas de carbo 1 unidade de insulina cobre)
    fator_insulina = st.number_input(
        "Fator de Sensibilidade/Carbo (g/U):", 
        min_value=1.0, value=15.0, step=1.0,
        help="Quantos gramas de carboidrato 1 unidade de NovoRapid cobre para você?"
    )
    st.divider()

    st.header("🛒 Adicionar Alimento")
    
    categorias_lista = sorted(list(alimentos_db.keys()))
    categoria_selecionada = st.selectbox("1. Categoria:", categorias_lista)
    
    alimentos_lista = sorted(list(alimentos_db[categoria_selecionada].keys()))
    alimento_selecionado = st.selectbox("2. Alimento:", alimentos_lista)
    
    dados_alimento = alimentos_db[categoria_selecionada][alimento_selecionado]
    opcoes_medida = ["Peso (g/ml)"]
    if dados_alimento["medidas"]:
        opcoes_medida.extend(list(dados_alimento["medidas"].keys()))
        
    tipo_medida = st.selectbox("3. Medição:", opcoes_medida)
    
    if tipo_medida == "Peso (g/ml)":
        quantidade = st.number_input("Insira o Peso (g/ml):", min_value=1.0, value=100.0, step=10.0)
        peso_final_g = quantidade
        desc_qtd = f"{quantidade:.1f}g"
    else:
        peso_unidade = dados_alimento["medidas"][tipo_medida]
        quantidade = st.number_input(f"Quantidade ({tipo_medida}):", min_value=0.5, value=1.0, step=0.5)
        peso_final_g = quantidade * peso_unidade
        desc_qtd = f"{quantidade}x {tipo_medida} (~{peso_final_g:.0f}g)"
    
    st.write("") # Espaço em branco
    if st.button("➕ Adicionar ao Prato", use_container_width=True, type="primary"):
        fator = peso_final_g / 100.0
        carbos_por_porcao = dados_alimento["carb"] * fator
        
        ig_alimento = dados_alimento["ig"]
        cg_alimento = (ig_alimento * carbos_por_porcao) / 100.0
        
        item = {
            "nome": alimento_selecionado.strip(),
            "descricao_qtd": desc_qtd,
            "peso_g": peso_final_g,
            "cal": dados_alimento["cal"] * fator,
            "carb": carbos_por_porcao,
            "prot": dados_alimento["prot"] * fator,
            "fat": dados_alimento["fat"] * fator,
            "ig": ig_alimento,
            "cg": cg_alimento
        }
        st.session_state.refeicao.append(item)
        
    st.divider()
    
    # === SESSÃO DE REFEIÇÕES SALVAS ===
    st.header("📂 Refeições Salvas")
    
    # 1. Carregar uma refeição existente
    opcoes_salvas = list(st.session_state.refeicoes_salvas_db.keys())
    if opcoes_salvas:
        ref_escolhida = st.selectbox("Carregar Refeição:", ["Selecione..."] + opcoes_salvas)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("📥 Carregar", use_container_width=True):
                if ref_escolhida != "Selecione...":
                    # Anexa os itens ou substitui o prato atual (aqui vamos substituir)
                    st.session_state.refeicao = st.session_state.refeicoes_salvas_db[ref_escolhida].copy()
                    st.success(f"Carregado: {ref_escolhida}")
                    st.rerun()
        with c2:
            if st.button("🗑️ Excluir", use_container_width=True):
                if ref_escolhida != "Selecione...":
                    st.session_state.refeicoes_salvas_db = remover_refeicao_do_disco(ref_escolhida)
                    st.success(f"Apagado: {ref_escolhida}")
                    st.rerun()
    else:
        st.info("Nenhuma refeição salva ainda.")
        
    # 2. Salvar o prato atual
    if st.session_state.refeicao:
        st.write("---")
        nome_salvar = st.text_input("Salvar prato atual como:")
        if st.button("💾 Salvar Prato Atual", use_container_width=True):
            if nome_salvar.strip() != "":
                st.session_state.refeicoes_salvas_db = salvar_refeicao_no_disco(nome_salvar, st.session_state.refeicao)
                st.success(f"Prato '{nome_salvar}' salvo com sucesso!")
                st.rerun()
            else:
                st.error("Digite um nome válido.")

# Função para colorir o IG
def classificar_ig(ig):
    if ig == 0: return ""
    elif ig <= 55: return "<span class='ig-baixo'>(IG Baixo)</span>"
    elif ig <= 69: return "<span class='ig-medio'>(IG Médio)</span>"
    else: return "<span class='ig-alto'>(IG Alto)</span>"

# =======================
# MAIN DASHBOARD
# =======================
if not st.session_state.refeicao:
    st.info("🍽️ **Seu prato está vazio.** Comece a pesquisar alimentos na lateral, ou carregue uma refeição salva na sessão 📂.")
else:
    # Calcular totais do prato
    totais = {"cal": 0, "carb": 0, "prot": 0, "fat": 0, "peso": 0, "cg": 0}
    for item in st.session_state.refeicao:
        totais["cal"] += item["cal"]
        totais["carb"] += item["carb"]
        totais["prot"] += item["prot"]
        totais["fat"] += item["fat"]
        totais["peso"] += item["peso_g"]
        totais["cg"] += item["cg"]
        
    # === Dashboard de Resumo no TOPO ===
    st.subheader("📊 Resumo da Refeição Atual")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🔥 Calorias", f"{totais['cal']:.0f} kcal")
    c2.metric("🍞 Carbos (Total)", f"{totais['carb']:.1f}g")
    c3.metric("📈 Carga Glicêmica", f"{totais['cg']:.1f}")
    c4.metric("🍗 Proteínas", f"{totais['prot']:.1f}g")
    
    # Cálculo Estimado de Insulina NovoRapid
    dose_recomendada = totais["carb"] / fator_insulina
    
    st.markdown(f"""
        <div class="insulin-box">
            <h4>💉 Dose Recomendada (NovoRapid)</h4>
            <h2>{dose_recomendada:.1f} U</h2>
            <p style="font-size:0.9em; margin:0; color:#555;">Baseado no Fator de {fator_insulina}g/U.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # === Lista de Itens do Prato ===
    colTitle, colWeight, colClear = st.columns([4, 2, 2])
    colTitle.subheader("📋 Itens Adicionados")
    colWeight.markdown(f"<p style='text-align:center; padding-top:10px;'>⚖ Peso: <b>{totais['peso']:.1f}g</b></p>", unsafe_allow_html=True)
    if colClear.button("🔄 Limpar Tudo", use_container_width=True):
        st.session_state.refeicao = []
        st.rerun()

    st.write("")

    for i, item in enumerate(st.session_state.refeicao):
        try:
            container = st.container(border=True)
        except TypeError:
            container = st.container()
            
        with container:
            col1, col2, col3, col4 = st.columns([3.5, 1.5, 3.5, 0.8])
            with col1:
                st.write(f"**{item['nome']}**")
                st.caption(f"_{item['descricao_qtd']}_")
            with col2:
                st.write(f"🍞 **{item['carb']:.1f}g**")
            with col3:
                ig_label = str(item['ig']) if item['ig'] > 0 else "0/Traços"
                st.markdown(f"**IG:** {ig_label} {classificar_ig(item['ig'])}", unsafe_allow_html=True)
                st.caption(f"Cal: {item['cal']:.0f} | P: {item['prot']:.1f} | G: {item['fat']:.1f}")
            with col4:
                st.write("")
                if st.button("❌", key=f"btn_{i}", help="Remover"):
                    st.session_state.refeicao.pop(i)
                    st.rerun()
