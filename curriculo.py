import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf():
    buffer = BytesIO()
    # Cria um arquivo PDF vazio
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # Informações pessoais
    c.setFont('Helvetica-Bold', 14)
    c.drawString(50, 750, "Currículo de Maria Clara Fontenele Silva")
    c.setFont('Helvetica', 12)
    c.drawString(50, 730, "fontenelesilvamariaclara@gmail.com | (61) 98160-7950")
    c.drawString(50, 710, "LinkedIn: Maria Clara - https://www.linkedin.com/in/mariaclara")
    c.drawString(50, 690, "Github: CraraMaria - https://github.com/CraraMaria")
    c.drawString(50, 670, "Nacionalidade: Brasileira | Idade: 23 anos | Estado Civil: Solteira")
    
    # Educação
    c.setFont('Helvetica-Bold', 12)
    c.drawString(50, 640, "Educação")
    education_data = [
        {
            'Período': '2023 - Presente',
            'Curso': 'Bacharelado em Ciência da Computação',
            'Instituição': 'Instituto de Educação Superior de Brasília (IESB)',
            'Localização': 'Brasília, DF',
        },
        {
            'Período': '2018 - 2021',
            'Curso': 'Pleno de Lingua Inglesa Estrangeira Moderna Inglês',
            'Instituição': 'Centro Interescolar de Línguas do Gama',
            'Localização': 'Gama, DF',
        }
    ]
    
    y_position = 620
    for education in education_data:
        c.setFont('Helvetica-Bold', 11)
        c.drawString(70, y_position, f"{education['Curso']} at {education['Instituição']}")
        c.setFont('Helvetica', 10)
        c.drawString(90, y_position - 20, f"Período: {education['Período']}")
        c.drawString(90, y_position - 40, f"Localização: {education['Localização']}")
        y_position -= 60
    
    # Síntese das Qualificações
    c.setFont('Helvetica-Bold', 12)
    c.drawString(50, y_position, "Síntese das Qualificações")
    qualifications_text = (
        "Profissional graduado em Tecnologia em Coaching e Desenvolvimento Humano, com mais de 4 anos de experiência na área, "
        "atuando em empresas multinacionais de grande porte, destacando-se os segmentos TI e bancário. Expertise em "
        "racionalização e redesenho de processos, incluindo desenvolvimento e integração entre sistemas, com utilização de alta "
        "tecnologia, gestão e plano de implantação. Experiência consolidada em criação, desenvolvimento, execução e análise testes, "
        "contribuindo para a garantia da qualidade dos sistemas. Participação ativa em programas de inovação e de melhoria contínua "
        "de produtos digitais, utilizando as metodologias ágeis (Scrum, KanBan) como facilitadoras e garantindo um portfólio "
        "moderno, diversificado e de alta qualidade. Forte atuação com operação e monitoramento de ambiente Mainframe, "
        "contando com a análise de incidentes críticos e suporte técnico ao usuário em diversos níveis de complexidade. Sólido "
        "conhecimento em elaboração de relatórios gerenciais, acompanhamento de indicadores de desempenho e fornecimento de "
        "subsídios para suporte em tomadas de decisões estratégicas. Profissional altamente capacitado para trabalhar em equipe, "
        "dedicado às funções, focado em resultados e redução de custos. Organizado, responsável e flexível."
    )
    text_objects = c.beginText(50, y_position - 40)
    text_objects.setFont("Helvetica", 10)
    text_objects.setLeading(14)
    text_objects.setTextOrigin(50, y_position - 40)
    text_objects.textLines(qualifications_text)
    c.drawText(text_objects)
    
    # Habilidades
    c.setFont('Helvetica-Bold', 12)
    c.drawString(50, 200, "Habilidades")
    skills = [
        'Python', 'SQL', 'Machine Learning', 'React', 'Git',
        'HTML/CSS', 'JavaScript', 'Django', 'Flask', 'Scikit-learn'
    ]
    skills_text = ", ".join(skills)
    c.setFont('Helvetica', 10)
    c.drawString(70, 180, skills_text)
    
    # Projetos
    c.setFont('Helvetica-Bold', 12)
    c.drawString(50, 160, "Projetos")
    project_data = [
        {
            'Nome do Projeto': 'Sistema de Gestão Escolar',
            'Descrição': 'Desenvolvimento de um sistema web para gestão de escolas utilizando Django.',
            'Tecnologias Utilizadas': 'Python, Django, HTML/CSS, PostgreSQL'
        },
        {
            'Nome do Projeto': 'Classificação de Texto com Machine Learning',
            'Descrição': 'Implementação de um modelo de classificação de texto utilizando técnicas de Machine Learning.',
            'Tecnologias Utilizadas': 'Python, Scikit-learn, NLTK, Jupyter Notebooks'
        }
    ]
    
    y_position = 140
    for project in project_data:
        c.setFont('Helvetica-Bold', 11)
        c.drawString(70, y_position, project['Nome do Projeto'])
        c.setFont('Helvetica', 10)
        c.drawString(90, y_position - 20, f"Descrição: {project['Descrição']}")
        c.drawString(90, y_position - 40, f"Tecnologias Utilizadas: {project['Tecnologias Utilizadas']}")
        y_position -= 60
    
    # Interesses e Atividades
    c.setFont('Helvetica-Bold', 12)
    c.drawString(50, y_position, "Interesses e Atividades")
    interests_text = (
        "- Participação em hackathons.\n"
        "- Desenvolvimento de projetos pessoais.\n"
        "- Leitura sobre novas tecnologias."
    )
    text_objects = c.beginText(50, y_position - 20)
    text_objects.setFont("Helvetica", 10)
    text_objects.setLeading(14)
    text_objects.setTextOrigin(50, y_position - 20)
    text_objects.textLines(interests_text)
    c.drawText(text_objects)
    
    # Salvando o PDF
    c.showPage()
    c.save()
    
    buffer.seek(0)
    return buffer

def main():
    st.title('Currículo de Maria Clara Fontenele')
    
    # Informações pessoais
    st.header('Informações Pessoais')
    st.write("""
        **Nome:** Maria Clara Fontenele  
        **Email:** fontenelesilvamariaclara@gmail.com  
        **Telefone:** (61) 98160-7950  
        **LinkedIn:** [Maria Clara](https://www.linkedin.com/in/mariaclara)   
        **Github:** [CraraMaria](https://github.com/CraraMaria)  
        **Nacionalidade:** Brasileira  
        **Idade:** 23 anos  
        **Estado Civil:** Solteira
    """)
    

    # Educação
    st.header('Educação')
    education_data = [
        {
            'Período': '2023 - Presente',
            'Curso': 'Bacharelado em Ciência da Computação',
            'Instituição': 'Instituto de Educação Superior de Brasília (IESB)',
            'Localização': 'Brasília, DF',
        },
        {
            'Período': '2018 - 2021',
            'Curso': 'Pleno de Lingua Inglesa Estrangeira Moderna Inglês',
            'Instituição': 'Centro Interescolar de Línguas do Gama',
            'Localização': 'Gama, DF',
        }
    ]
    
    for education in education_data:
        st.subheader(f"{education['Curso']} at {education['Instituição']}")
        st.write(f"**Período:** {education['Período']}")
        st.write(f"**Localização:** {education['Localização']}")
    
    # Síntese das Qualificações
    st.header('Síntese das Qualificações')
    qualifications_text = (
        "Profissional em graduação em Ciência da Computação, no quarto semestre, destacando interesse os segmentos TI, desenvolvimento, ciência de dados e educação."
        "Expertise em em programação Python, desenvolvimento web com Django, análise de dados com Pandas, visualização de dados com Matplotlib e criação de modelos de Machine Learning utilizando Scikit-learn")
    st.write(qualifications_text)
    
    # Habilidades
    st.header('Habilidades')
    skills = [
        'Python', 'SQL', 'Machine Learning', 'React', 'Git',
        'HTML/CSS', 'JavaScript', 'Django', 'Flask', 'Scikit-learn'
    ]
    st.write(', '.join(skills))

    # Projetos
    st.header('Projetos')
    project_data = [
        {
            'Nome do Projeto': 'Sistema de Gestão Escolar',
            'Descrição': 'Desenvolvimento de um sistema web para gestão de escolas utilizando Django.',
            'Tecnologias Utilizadas': 'Python, Django, HTML/CSS, PostgreSQL'
        },
        {
            'Nome do Projeto': 'Classificação de Texto com Machine Learning',
            'Descrição': 'Implementação de um modelo de classificação de texto utilizando técnicas de Machine Learning.',
            'Tecnologias Utilizadas': 'Python, Scikit-learn, NLTK, Jupyter Notebooks'
        }
    ]

    for project in project_data:
        st.subheader(project['Nome do Projeto'])
        st.write(f"**Descrição:** {project['Descrição']}")
        st.write(f"**Tecnologias Utilizadas:** {project['Tecnologias Utilizadas']}")

    # Interesses e atividades
    st.header('Interesses e Atividades')
    st.write("""
        - Participação em hackathons.
        - Desenvolvimento de projetos pessoais.
        - Leitura sobre novas tecnologias.
    """)

    # Botão para download do currículo em PDF
    st.markdown("[Baixar Currículo em PDF](#)")

    # Para fazer o download do PDF
    if st.button('Curriculo PDF'):
        pdf_file = generate_pdf()
        st.download_button(
            label="Baixar Currículo em PDF",
            data=pdf_file,
            file_name='curriculo_maria_clara.pdf',
            mime='application/pdf'
        )

if __name__ == '__main__':
    main()
