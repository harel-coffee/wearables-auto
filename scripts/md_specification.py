import numpy as np

voi = {
    'age_enroll': (['22nan', 'mean_impute'], 'continuous'),
    'marital': (['nan27', 'binarize_is_2.0'], 'categorical'),
    'gestage_by': (['nan2-99'], 'categorical'),
    'insur': (['nan2-99'], 'categorical'),
    'ethnicity': (['nan23', 'binarize_not_1'], 'categorical'),
    'race': (['nan27', 'binarize_not_2'], 'categorical'),
    'bmi_1vis': (['absval', 'mean_impute'], 'continuous'),
    'prior_ptb_all': (['nan25', '5to1', '4to1', 'binarize_not_1.0'],
    'categorical'),
    'fullterm_births': (['nan25', '5to1', 'binarize_is_1.0'], 'categorical'),
    'surghx_none': (['nan20'], 'categorical'),
    'alcohol': (['nan22', '2to0'], 'categorical'),
    'smoke': (['nan22', '2to0'], 'categorical'),
    'drugs': (['nan22', '2to0'], 'categorical'),
    'hypertension': (['nan22', '2to0'], 'categorical'),
    'pregestational_diabetes': (['nan22', '2to0'], 'categorical'),
    'asthma_yes___1': (['binarize_is_1'], 'categorical'),
    'asthma_yes___2': (['binarize_is_1'], 'categorical'),
    'asthma_yes___3': (['binarize_is_1'], 'categorical'),
    'asthma_yes___4': (['binarize_is_1'], 'categorical'),
    'asthma_yes___5': (['binarize_is_1'], 'categorical'),
    'asthma_yes___7': (['binarize_is_1'], 'categorical'),
    'asthma_yes___8': (['binarize_is_1'], 'categorical'),
    'asthma_yes___10': (['binarize_is_1'], 'categorical'),
    'asthma_yes___13': (['binarize_is_1'], 'categorical'),
    'asthma_yes___18': (['binarize_is_1'], 'categorical'),
    'asthma_yes___19': (['binarize_is_1'], 'categorical'),
    'asthma_yes___20': (['binarize_is_1'], 'categorical'),
    'other_disease': (['nan22', '2to0'], 'categorical'),
    'gestational_diabetes': (['nan22', '2to0', 'binarize_is_1.0'], 'categorical'),
    'ghtn': (['nan22', '2to0', 'binarize_is_1.0'], 'categorical'),
    'preeclampsia': (['nan22', '2to0', 'binarize_is_1.0'], 'categorical'),
    'rh': (['nan22', '2to0', 'binarize_is_1.0'], 'categorical'),
    'corticosteroids': (['nan22', '2to0', 'binarize_is_1.0'], 'categorical'),
    'abuse': (['nan23', '3to0', 'binarize_is_1.0'], 'categorical'),
    'assist_repro': (['nan23', '3to0', 'binarize_is_1.0'], 'categorical'),
    'gyn_infection': (['nan22', '2to0', 'binarize_is_1.0'], 'categorical'),
    'maternal_del_weight': (['-992nan', '-882nan', 'mean_impute'], 'continuous'),
    'ptb_37wks': (['nan22', '2to0', 'binarize_is_1.0'], 'categorical'),
    'cbc_hct': (['-992nan', 'mean_impute'], 'continuous'),
    'cbc_wbc': (['-992nan', 'mean_impute'], 'continuous'),
    'cbc_plts': (['-992nan', 'mean_impute'], 'continuous'),
    'cbc_mcv': (['-992nan', 'mean_impute'], 'continuous'),
    'art_pco2': (['-992nan', 'mean_impute'], 'continuous'),
    'art_po2': (['-992nan', 'mean_impute'], 'continuous'),
    'art_excess': (['-992nan', 'mean_impute'], 'continuous'),
    'art_lactate': (['-992nan', 'mean_impute'], 'continuous'),
    'ven_ph': (['-992nan', 'mean_impute'], 'continuous'),
    'ven_pco2': (['-992nan', 'mean_impute'], 'continuous'),
    'ven_po2': (['-992nan', 'mean_impute'], 'continuous'),
    'ven_lactate': (['-992nan', 'mean_impute'], 'continuous'),
    'anes_type': (['nan21'], 'categorical'),
    'epidural': (['nan20'], 'categorical'),
    'deliv_mode': (['nan24'], 'categorical'),
    'infant_wt': (['-992nan', 'mean_impute'], 'continuous'),
    'infant_length': (['-992nan', 'mean_impute'], 'continuous'),
    'head_circ': (['-992nan', 'mean_impute'], 'continuous'),
    'death_baby': (['nan20'], 'categorical'),
    'neonatal_complication': (['22nan', 'nan20'], 'categorical'),
    'ervisit': (['nan20'], 'categorical'),
    'ppvisit_dx': (['nan26', 'binarize_not_7.0'], 'categorical'),
    'education': (['nan2-99'], 'categorical'),
    'paidjob1': (['nan20'], 'categorical'),
    'work_hrs1': (['nan2-99'], 'categorical'),
    'income_annual1': (['nan2-99', '3to1', '2to1', '10to1', 'binarize_is_1'],
    'categorical'),
    'income_support1': (['nan2-99', '2to1', 'binarize_not_1'], 'categorical'),
    'regular_period1': (['nan2-88', '-88to1'], 'categorical'),
    'period_window1': (['nan2-88'], 'categorical'),
    'menstrual_days1': (['nan2-88'], 'categorical'),
    'bc_past1': (['nan20'], 'categorical'),
    'bc_years1': (['882nan', '-882nan', 'mean_impute'], 'continuous'),
    'months_noprego1': (['nan24', 'binarize_is_1'], 'categorical'),
    'premature_birth1': (['nan2-88'], 'categorical'),
    'stress1_1': (['nan2-99'], 'categorical'),
    'stress2_1': (['nan2-99'], 'categorical'),
    'stress3_1': (['nan2-99'], 'categorical'),
    'stress4_1': (['nan2-99'], 'categorical'),
    'stress5_1': (['nan2-99'], 'categorical'),
    'stress6_1': (['nan2-99'], 'categorical'),
    'stress7_1': (['nan2-99'], 'categorical'),
    'stress8_1': (['nan2-99'], 'categorical'),
    'stress9_1': (['nan2-99'], 'categorical'),
    'stress10_1': (['nan2-99'], 'categorical'),
    'workreg_1trim': (['nan2-99'], 'categorical'),
    'choosesleep_1trim': (['nan2-99'], 'categorical'),
    'slpwake_1trim': (['nan2-99'], 'categorical'),
    'slp30_1trim': (['nan2-99'], 'categorical'),
    'sleep_qual1': (['nan2-99'], 'categorical'),
    'slpenergy1': (['nan2-99'], 'categorical'),
    'sitting1': (['nan2-99'], 'categorical'),
    'tv1': (['nan2-99'], 'categorical'),
    'inactive1': (['nan2-99'], 'categorical'),
    'passenger1': (['nan2-99'], 'categorical'),
    'reset1': (['nan2-99'], 'categorical'),
    'talking1': (['nan2-99'], 'categorical'),
    'afterlunch1': (['nan2-99'], 'categorical'),
    'cartraffic1': (['nan2-99'], 'categorical'),
    'edinb1_1trim': (['nan2-99'], 'categorical'),
    'edinb2_1trim': (['nan2-99'], 'categorical'),
    'edinb3_1trim': (['nan2-99'], 'categorical'),
    'edinb4_1trim': (['nan2-99'], 'categorical'),
    'edinb5_1trim': (['nan2-99'], 'categorical'),
    'edinb6_1trim': (['nan2-99'], 'categorical'),
    'edinb7_1trim': (['nan2-99'], 'categorical'),
    'edinb8_1trim': (['nan2-99'], 'categorical'),
    'edinb9_1trim': (['nan2-99'], 'categorical'),
    'edinb10_1trim': (['nan2-99'], 'categorical')
}

# md_v522_210124.csv
omit_cols = ['index', 'record_id', 'pid', 'Absolute Error', 'GA', 'y', 'visit_num', 'yhat', 'Pre-term birth', 'split', 'error'] + ['Error group']

mdpred_voi = {
    'age_enroll': 'continuous',
    'marital': 'categorical',
    'gestage_by': 'categorical',
    'insur': 'categorical',
    'ethnicity': 'categorical',
    'race': 'categorical',
    'bmi_1vis': 'continuous',
    'prior_ptb_all': 'categorical',
    'fullterm_births': 'categorical',
    'surghx_none': 'categorical',
    'alcohol': 'categorical',
    'smoke': 'categorical',
    'drugs': 'categorical',
    'hypertension': 'categorical',
    'pregestational_diabetes': 'categorical',
    'asthma_yes___1': 'categorical',
    'asthma_yes___2': 'categorical',
    'asthma_yes___3': 'categorical',
    'asthma_yes___4': 'categorical',
    'asthma_yes___5': 'categorical',
    'asthma_yes___7': 'categorical',
    'asthma_yes___8': 'categorical',
    'asthma_yes___10': 'categorical',
    'asthma_yes___13': 'categorical',
    'asthma_yes___18': 'categorical',
    'asthma_yes___19': 'categorical',
    'asthma_yes___20': 'categorical',
    'other_disease': 'categorical',
    'gestational_diabetes': 'categorical',
    'ghtn': 'categorical',
    'preeclampsia': 'categorical',
    'rh': 'categorical',
    'corticosteroids': 'categorical',
    'abuse': 'categorical',
    'assist_repro': 'categorical',
    'gyn_infection': 'categorical',
    'maternal_del_weight': 'continuous',
    'ptb_37wks': 'categorical',
    'cbc_hct': 'continuous',
    'cbc_wbc': 'continuous',
    'cbc_plts': 'continuous',
    'cbc_mcv': 'continuous',
    'art_pco2': 'continuous',
    'art_po2': 'continuous',
    'art_excess': 'continuous',
    'art_lactate': 'continuous',
    'ven_ph': 'continuous',
    'ven_pco2': 'continuous',
    'ven_po2': 'continuous',
    'ven_lactate': 'continuous',
    'anes_type': 'categorical',
    'epidural': 'categorical',
    'deliv_mode': 'categorical',
    'infant_wt': 'continuous',
    'infant_length': 'continuous',
    'head_circ': 'continuous',
    'death_baby': 'categorical',
    'neonatal_complication': 'categorical',
    'ervisit': 'categorical',
    'ppvisit_dx': 'categorical',
    'education': 'categorical',
    'paidjob1': 'categorical',
    'work_hrs1': 'categorical',
    'income_annual1': 'categorical',
    'income_support1': 'categorical',
    'regular_period1': 'categorical',
    'period_window1': 'categorical',
    'menstrual_days1': 'categorical',
    'bc_past1': 'categorical',
    'bc_years1': 'continuous',
    'months_noprego1': 'categorical',
    'premature_birth1': 'categorical',
    'stress1_1': 'categorical',
    'stress2_1': 'categorical',
    'stress3_1': 'categorical',
    'stress4_1': 'categorical',
    'stress5_1': 'categorical',
    'stress6_1': 'categorical',
    'stress7_1': 'categorical',
    'stress8_1': 'categorical',
    'stress9_1': 'categorical',
    'stress10_1': 'categorical',
    'workreg_1trim': 'categorical',
    'choosesleep_1trim': 'categorical',
    'slpwake_1trim': 'categorical',
    'slp30_1trim': 'categorical',
    'sleep_qual1': 'categorical',
    'slpenergy1': 'categorical',
    'sitting1': 'categorical',
    'tv1': 'categorical',
    'inactive1': 'categorical',
    'passenger1': 'categorical',
    'reset1': 'categorical',
    'talking1': 'categorical',
    'afterlunch1': 'categorical',
    'cartraffic1': 'categorical',
    'edinb1_1trim': 'categorical',
    'edinb2_1trim': 'categorical',
    'edinb3_1trim': 'categorical',
    'edinb4_1trim': 'categorical',
    'edinb5_1trim': 'categorical',
    'edinb6_1trim': 'categorical',
    'edinb7_1trim': 'categorical',
    'edinb8_1trim': 'categorical',
    'edinb9_1trim': 'categorical',
    'edinb10_1trim': 'categorical',
    'IS': 'continuous',
    'IV': 'continuous',
    'RA': 'continuous',
    'ISm': 'continuous',
    'IVm': 'continuous',
    'min_rest': 'continuous',
    'ave_logpseudocount_wake': 'continuous',
    'ave_logpseudocount_sleep': 'continuous',
    'ave_logpseudocount_wknd': 'continuous',
    'ave_logpseudocount_wkday': 'continuous',
    'ave_logpseudocount_day': 'continuous',
    'ave_logpseudocount_night': 'continuous',
    'PQSI': 'continuous',
    'KPAS': 'continuous',
    'EpworthSS': 'continuous',
    'Edinburgh': 'continuous',
}