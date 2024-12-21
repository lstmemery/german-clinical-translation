#! /usr/bin/fish

function render_docx
    quarto render notebooks/process_modelling.qmd -P model:../models/$argv[1].json -t docx --output $argv[1].docx
    mv $argv[1].docx output
end

render_docx del_ersq_t_phq9
render_docx del_ders_t_phq9

render_docx t1_ders_s_h49b
render_docx t1_ders_t_h49b
render_docx t1_ders_s_phq9
render_docx t1_ders_t_phq9

render_docx t1_ersq_s_h49b
render_docx t1_ersq_t_h49b
render_docx t1_ersq_s_phq9
render_docx t1_ersq_t_phq9

render_docx t1_ders_l_h49b
render_docx t1_ders_l_phq9
render_docx t1_ersq_l_h49b
render_docx t1_ersq_l_phq9
