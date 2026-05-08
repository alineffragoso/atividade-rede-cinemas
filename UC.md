# Casos de Uso – Sistema Rede de Cinemas

## Atores do Sistema

### Administrador
Responsável pelo gerenciamento de filmes, sessões e controle de público.

### Espectador
Responsável pela consulta de filmes e horários das sessões.

---

# UC01 – Cadastrar Cinema

## Ator Principal
Administrador

## Descrição
Permite cadastrar uma nova unidade de cinema no sistema.

## Fluxo Principal

1. O administrador acessa a tela de cadastro de cinema.
2. O sistema solicita os dados do cinema.
3. O administrador informa nome, endereço, cidade, estado e capacidade.
4. O sistema valida os dados.
5. O sistema salva o cinema.
6. O sistema exibe mensagem de sucesso.

## Fluxo Alternativo

4a. Caso algum campo obrigatório esteja vazio:
- O sistema exibe mensagem de erro.
- O cadastro não é realizado.

---

# UC02 – Cadastrar Filme

## Ator Principal
Administrador

## Descrição
Permite cadastrar filmes que serão exibidos nos cinemas.

## Fluxo Principal

1. O administrador acessa a tela de cadastro de filme.
2. O sistema solicita os dados do filme.
3. O administrador informa título, duração, gênero, diretor e elenco.
4. O sistema valida as informações.
5. O sistema salva o filme.
6. O sistema exibe mensagem de sucesso.

## Fluxo Alternativo

4a. Caso a duração do filme seja inválida:
- O sistema exibe mensagem de erro.
- O cadastro não é concluído.

---

# UC03 – Cadastrar Sessão

## Ator Principal
Administrador

## Descrição
Permite cadastrar sessões para exibição dos filmes.

## Fluxo Principal

1. O administrador acessa a tela de cadastro de sessão.
2. O sistema solicita os dados da sessão.
3. O administrador seleciona cinema, filme e horário.
4. O sistema verifica disponibilidade do horário.
5. O sistema valida intervalo entre sessões.
6. O sistema salva a sessão.
7. O sistema exibe mensagem de sucesso.

## Fluxo Alternativo

4a. Caso exista conflito de horário:
- O sistema informa indisponibilidade.
- A sessão não é cadastrada.

---

# UC04 – Registrar Público

## Ator Principal
Administrador

## Descrição
Permite registrar a quantidade de espectadores presentes em uma sessão.

## Fluxo Principal

1. O administrador acessa a sessão desejada.
2. O sistema solicita quantidade de espectadores.
3. O administrador informa o total de público.
4. O sistema valida capacidade do cinema.
5. O sistema salva o registro.
6. O sistema exibe confirmação.

## Fluxo Alternativo

4a. Caso o público ultrapasse a capacidade:
- O sistema exibe mensagem de erro.
- O registro não é salvo.

---

# UC05 – Consultar Filmes em Cartaz

## Ator Principal
Espectador

## Descrição
Permite visualizar os filmes disponíveis nos cinemas.

## Fluxo Principal

1. O espectador acessa a área de filmes.
2. O sistema exibe lista de filmes em cartaz.
3. O espectador visualiza informações do filme.
4. O sistema apresenta gênero, duração e diretor.

---

# UC06 – Consultar Sessões

## Ator Principal
Espectador

## Descrição
Permite visualizar horários das sessões disponíveis.

## Fluxo Principal

1. O espectador acessa a área de sessões.
2. O sistema exibe sessões disponíveis.
3. O espectador seleciona um filme.
4. O sistema apresenta horários e cinemas disponíveis.

---

# UC07 – Consultar Relatório de Público

## Ator Principal
Administrador

## Descrição
Permite visualizar total de público por filme e por cinema.

## Fluxo Principal

1. O administrador acessa área de relatórios.
2. O sistema solicita tipo de relatório.
3. O administrador seleciona relatório desejado.
4. O sistema calcula os dados.
5. O sistema apresenta os resultados.
