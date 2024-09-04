# Social media simulation

Implementation order:
User > Post > Messages > Post Comments
## Scope:

BaseModel:
id: int, pk
created_at: datetime, auto
updated_at: datetime, auto


 - Message
   - sender: User
   - receiver: User
   - message: text
  
 - Post
    - user: User
    - content: text
    - media: url
    - likes: list[Like]
    - Tags: list[str]

 - User
   - name
   - birthday
   - Sex
     - male
     - female
     - another
   - Religions
     - Cristianismo
     - Islamismo
     - Judaísmo
     - Budismo
     - Hinduísmo
     - Sikhismo
     - Espiritismo
     - Espiritualismo
     - Religiões Afro-Brasileiras (Candomblé, Umbanda)
     - Xintoísmo
     - Taoísmo
     - Jainismo
     - Zoroastrismo
     - Baha'í
     - Ateísmo
     - Agnosticismo
     - Neo-Paganismo (Wicca, Druidismo, etc.)
     - Religiões Indígenas
     - Nova Era
   - Interests and Hobbies
      - Tecnologia e Gadgets
      - Gaming (Videogames)
      - Esportes e Fitness
      - Música
      - Cinema e Séries de TV
      - Leitura e Literatura
      - Fotografia
      - Viagens
      - Gastronomia (Culinária)
      - Moda e Beleza
      - Artes e Artesanato
      - Jardinagem
      - DIY (Faça Você Mesmo)
      - Animais de Estimação
      - Colecionismo
      - Carros e Automobilismo
      - Meditação e Bem-estar
      - Voluntariado e Ativismo
      - História e Cultura
      - Ciência e Inovação
      - Educação e Aprendizado Contínuo
      - Investimentos e Finanças Pessoais
      - Fotografia
      - Blogging e Vlogging
      - Astrologia
      - Ciclismo
      - Esportes Radicais
      - Moda Sustentável
      - Ecologia e Sustentabilidade
      - Festas e Eventos Sociais
      - Artes Marciais
      - Brinquedos e Jogos de Tabuleiro
      - Construção de Modelos e Maquetes
      - Poesia e Escrita Criativa
      - Arquitetura e Design de Interiores
      - Programação e Desenvolvimento de Software
      - Cultura Pop e Fandoms
      - Quadrinhos e Mangás
      - Astronomia
   - values and beliefs
      - Political ideology:
        - Conservadorismo
        - Liberalismo
        - Socialismo
        - Anarquismo
        - Ambientalismo
      - Religious Beliefs:
        - Cristianismo
        - Islamismo
        - Judaísmo
        - Budismo
        - Hinduísmo
        - Espiritualismo
        - Ateísmo
        - Agnosticismo
      - Cultural Values:
        - Tradição vs. Modernidade
        - Coletivismo vs. Individualismo
        - Nacionalismo
        - Globalismo
      - Ethics:
        - Defensores dos Direitos Humanos
        - Vegetarianismo/Veganismo
        - Ética Profissional
        - Justiça Social
        - Igualdade de Gênero
        - Direitos LGBTQIA+
      - Philosophy of life:
        - Minimalismo
        - Materialismo
        - Humanismo
        - Hedonismo
        - Estoicismo
      - Family values:
        - Tradições familiares
        - Estruturas familiares (familia nuclear vs famílias estendidas)
        - Parentalidade ativa
      - Conspiracy Theories:
        - Teorias sobre controle governamental
        - Crenças em extraterrestres
        - Desconfiança nas vacinas
   - Social status
      - Influenciadores Digitais
      - Celebridades
      - Ativistas e Líderes Comunitários
      - Usuários Comuns
      - Usuários Anônimos
      - Influenciadores de Nicho
   - Professional
      - Executivos e Empresários
      - Profissionais CLT
      - Funcionários Públicos
      - Trabalhadores Informais
      - Trabalhadores manuais
      - Trabalhadores Criativos
      - Acadêmicos e Pesquisadores
      - Profissionais de Saúde
      - Estudantes
      - Desempregados
      - Empreendedores
      - Aposentados
   - Psychological
      - Extroversão vs. Introversão
      - Abertura a Novas Experiências
      - Amabilidade
      - Neuroticismo
      - Autoestima
      - Empatia
      - Assertividade
      - Curiosidade Social
      - Tendência a Seguir Normas
      - Impulsividade
      - Tendência à Comparação Social
   - Education
      - Nível de Escolaridade
      - Curso
   - Socioeconomic situation
      - Mora com família / republica / sozinho
      - Ocupaçao (Emprego, estudo)
      - esporte
   - Geographic locations of activities (living, study, sport or work) (List)


## Simulations (Must be done using AI)
 - Users can create posts
 - Users can comment in posts (mainly from friends)
 - Users can send and receive message on direct and view the chat

 - Criar variações de simulações (em guerra, extremamente engraçado, cheios de conflitos, cheios de romance/pegação, cheios de disputa, sem noção)
 - Avaliar a possibilidade de gerar fotos para os perfis
 - Simulação deverá ser feita inicialmente com 5000 perfis.



### Ideias posteriores
 - País, cidade e estado terem características culturais
 - Acontecimentos regionais ou globais e seus impactos


### Requisitos técnicos
 - Poetry (x)
 - API REST (/)
 - API assíncrona(x)
 - Testes de unidade
 - Testes de integração(/)
 - Testes de carga
 - CI
 - Migrações
 - Ambientes de dev (local) e prod (nuvem)
 - Banco de dados postgres
 - Docker-compose
 - Kafka

Talvez depois:
 - frontend
 - Kubernetes
