import pandas as pd
import scipy.stats
import streamlit as st
import time

#Estas son variables de estado que se conservan cuando Streamlit vuelve a ejecutar el script
if "experiment_no" not in st.session_state:
    st.session_state["experiment_no"] = 0

if "df_experiment_result" not in st.session_state:
    st.session_state["df_experiment_result"] = pd.DataFrame(columns=["no", "iteraciones", "media"])

st.header("Lanzar una moneda")

chart = st.line_chart([0.5])

#función que emula el lanzamiento de una moneda
def toss_coin(n): 
#The bernoulli distribution has only 2 outcomes 1(success) and 0(failure) probability of success p
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n) 

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

number_of_trials = st.slider("¿Número de intentos?", 1, 1000, 10)
start_button = st.button("Ejecutar")

if start_button:
    st.write(f"Experimento con {number_of_trials} intentos en curso.")
    st.session_state["experiment_no"] += 1
    mean = toss_coin(number_of_trials)
    st.session_state["df_experiment_results"] = pd.concat([
        st.session_state["df_experiment_results"],
        pd.DataFrame(data=[[st.session_state["experiment_no"],
                            number_of_trials,
                            mean]],
                            columns=["no", "iteration", "mean"])
    ]
    axis=0)
    st.session_state["df_experiment_results"] = st.session_state["df_experiment_results"].reset_index(drop=True)

st.write(st.session["df_experiment_results"])