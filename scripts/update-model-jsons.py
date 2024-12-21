from subprocess import call

model_strings = (
    '../models/ceas_from_hierarchical.json',
    '../models/ceas_from_one_factor.json',
    '../models/ceas_from_two_factor.json',
    '../models/ceas_sc_one_factor.json',
    '../models/ceas_sc_second_order.json',
    '../models/ceas_sc_third_order.json',
    '../models/ceas_sc_three_factor.json',
    '../models/ceas_sc_two_factor.json',
    '../models/ceas_to_hierarchical.json',
    '../models/ceas_to_one_factor.json',
    '../models/ceas_to_two_factor.json',
)

input_regexes = (
    'CEAS_FROM(\d+)_(\d+)',
    'CEAS_FROM(\d+)_(\d+)',
    'CEAS_FROM(\d+)_(\d+)',
    'CEAS_SC(\d+)_(\d+)',
    'CEAS_SC(\d+)_(\d+)',
    'CEAS_SC(\d+)_(\d+)',
    'CEAS_SC(\d+)_(\d+)',
    'CEAS_SC(\d+)_(\d+)',
    'CEAS_TO(\d+)_(\d+)',
    'CEAS_TO(\d+)_(\d+)',
    'CEAS_TO(\d+)_(\d+)',
)

output_prepends = (
    'T1_CEAS_FR',
    'T1_CEAS_FR',
    'T1_CEAS_FR',
    'T1_CEAS_S',
    'T1_CEAS_S',
    'T1_CEAS_S',
    'T1_CEAS_S',
    'T1_CEAS_S',
    'T1_CEAS_O',
    'T1_CEAS_O',
    'T1_CEAS_O',
)


for model_string, input_regex, output_prepend in list(zip(model_strings, input_regexes, output_prepends)):
    print(model_string)
    call(['python', 'update-model-json.py', model_string, input_regex, output_prepend])
    