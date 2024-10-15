# Psiu

João Pedro Duarte da Cunha - 2212840<br>
Link Site: http://18.214.253.160/

## O site

O Psiu é uma aplicação de eventos para alunos universitários. Um usuário pode ver/participar de atividades e eventos em 5 categorias:

- Caronas 
- Grupos de Estudos
- Atividades extracurriculares
- Ligas Acadêmicas
- E outras atividades sociais com foco em conhecer pessoas

Essas atividades possuem informações específicas a elas e um local e data para acontecer, sendo que um usuário pode se juntar a uma atividade se assim desejar.

## Os Eventos

Existem diversas ações que um usuário pode fazer com cada dos tipos de eventos:

Se o usuário não estiver autenticado:
- Visualizar a lista de eventos de um tipo específico
- Visualizar um evento
- Ver participantes/criador do evento
- Ver a data na qual esse evento vai ocorrer e em quanto tempo
- Visualizar o perfil do criador/participantes do evento

Se o usuário estiver autenticado:
- Criar um Evento
- Participar de um Evento
- Cancelar participação em um evento

Se o usuário for o criador do evento:
- Editar o evento
- Apagar o evento

## Os Usuários

Existem diversas operações relacionadas à usuários implementadas:
- Registro
- Login
- Logout
- Perfil
- Alteração de dados adicionais
- Alteração de senha
- Recuperação de senha

Além disso, os outros usuários podem visualizar o perfil dos usuários do site e ver em quais eventos um usuário está participando ou quais eventos um usuário criou.

## Funcionamento do Site

1. Se conectar a http://18.214.253.160/
2. Usar a barra superior para Registrar-se no site
3. Preencher as informações adicionais
4. Selecionar um dos tipos de eventos
5. Criar uma Atividade
6. Pode-se testar a edição/remoção da atividade
7. Selecione uma atividade não criada pelo usuário
8. Pode se testar a participação/cancelamento de participação em uma atividade

## Testagem

Quanto ao funcionamento do site, o site foi publicado usando o AWS e acredito que todas as funcionalidades mencionadas acima estão funcionando como esperado sendo que não encontrei aspectos não funcionais. A recuperação de senha foi implementada utilizando o painel do terminal para envio do email como o Gmail tem proteção para envios automatizados.
