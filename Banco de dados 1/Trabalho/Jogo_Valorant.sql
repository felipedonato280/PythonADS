-- TABELAS

-- CRIA A TABELA RANK DO JOGO (NAO PODE SER SO RANK PQ NO POSTGRE RANK É UM COMANDO)
CREATE TABLE Rank_Jogo (
  ID_Rank SERIAL PRIMARY KEY,
  Niveis_de_Rank VARCHAR(20) NOT NULL,
  Pontuacao INT
);

-- CRIA A TABELA JOGADOR
CREATE TABLE Jogador (
  ID_Jogador SERIAL PRIMARY KEY,
  Nome VARCHAR(50) NOT NULL,
  Nivel INT NOT NULL,
  ID_Rank INT NOT NULL,
  FOREIGN KEY (ID_Rank) REFERENCES Rank_Jogo(ID_Rank) ON UPDATE CASCADE ON DELETE CASCADE
);

-- CRIA A TABELA DO JOGO
CREATE TABLE Jogo (
  ID_Jogo SERIAL PRIMARY KEY,
  Genero VARCHAR(255) NOT NULL,
  Desenvolvedora VARCHAR(100) NOT NULL
);

-- CRIA A TABELA POSSUI (TABELA VINDA DE UM RELACIONAMENTO N:N)
CREATE TABLE Possui (
  ID_Jogo INT NOT NULL,
  ID_Jogador INT NOT NULL,
  PRIMARY KEY (ID_Jogo, ID_Jogador),
  FOREIGN KEY (ID_Jogo) REFERENCES Jogo(ID_Jogo) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (ID_Jogador) REFERENCES Jogador(ID_Jogador) ON UPDATE CASCADE ON DELETE CASCADE
);

-- CRIA A TABELA PARTIDA
CREATE TABLE Partida (
  ID_Partida SERIAL PRIMARY KEY,
  Duracao_da_Partida TIME NOT NULL,
  Placar INT NOT NULL,
  Mapa VARCHAR(50) NOT NULL
);

-- CRIA A TABELA JOGA TAMBEM VINDA DE UM RELACIONAMENTO N:N
CREATE TABLE Joga (
  ID_Jogador INT NOT NULL,
  ID_Partida INT NOT NULL,
  Eliminacoes INT DEFAULT 0,
  Assistencias INT DEFAULT 0,
  Mortes INT DEFAULT 0,
  PRIMARY KEY (ID_Jogador, ID_Partida),
  FOREIGN KEY (ID_Jogador) REFERENCES Jogador(ID_Jogador) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (ID_Partida) REFERENCES Partida(ID_Partida) ON UPDATE CASCADE ON DELETE CASCADE
);

-- CRIA A TABELA DOS ROUNDS
CREATE TABLE Round (
  ID_Round SERIAL PRIMARY KEY,
  Vencedor_Round BOOLEAN NOT NULL,
  Duracao_Round TIME NOT NULL,
  Numero_Round INT NOT NULL,
  ID_Partida INT NOT NULL,
  FOREIGN KEY (ID_Partida) REFERENCES Partida(ID_Partida) ON UPDATE CASCADE ON DELETE CASCADE
);

-- INSERTS

-- INSERE OS RANKS E O QUANTO FALTA PARA SUBIR
INSERT INTO Rank_Jogo (Niveis_de_Rank, Pontuacao) VALUES
('Ferro', 23),
('Bronze', 54),
('Prata', 71),
('Ouro', 90),
('Platina', 12),
('Diamante', 15),
('Ascendente', 18),
('Imortal', 22),
('Radiante', 26);

-- INSERE OS JOGADORES E SEUS DADOS
INSERT INTO Jogador (Nome, Nivel, ID_Rank) VALUES
('SennHack', 207, 9),
('Perseu', 40, 9),
('Jinxx', 18, 8),
('Riven', 55, 7),
('Shadow', 12, 2);

-- INSERE O JOGO E GENERO
INSERT INTO Jogo (Genero, Desenvolvedora) VALUES
('FPS Tático', 'Riot Games'),
('MOBA', 'Riot Games'),
('FPS Tático', 'Valve'),
('Card Game', 'Riot Games');

-- INSERE O JOGO QUE CADA JOGADOR POSSUI (TODOS VALORANT PQ É BOM)
INSERT INTO Possui (ID_Jogo, ID_Jogador) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5);

-- INSERE OS DADOS DA PARTIDA (DURACAO, PLACAR E MAPA)
INSERT INTO Partida (Duracao_da_Partida, Placar, Mapa) VALUES
('00:34:20', 13, 'Ascent'),
('00:29:55', 10, 'Bind'),
('00:41:12', 14, 'Icebox');

-- INSERE DESEMPENHO DO JOGADOR NA PARTIDA, TABELA VINDA DE UM RELACIONAMENTO N:N
INSERT INTO Joga (ID_Jogador, ID_Partida, Eliminacoes, Assistencias, Mortes) VALUES
(1, 1, 22, 5, 15),
(2, 1, 30, 7, 10),
(3, 1, 11, 3, 18),
(1, 2, 15, 2, 12),
(4, 2, 28, 4, 8),
(2, 3, 33, 9, 14),
(5, 3, 7, 1, 20);

-- INSERE DADOS DO ROUND MAPA ASCENT
INSERT INTO Round (Vencedor_Round, Duracao_Round, Numero_Round, ID_Partida) VALUES
(TRUE, '00:01:15', 1, 1),
(FALSE, '00:01:05', 2, 1),
(TRUE, '00:01:10', 3, 1),
(TRUE, '00:01:20', 4, 1),
(FALSE, '00:01:07', 5, 1);

-- INSERE DADOS DO ROUN MAPA BIND
INSERT INTO Round (Vencedor_Round, Duracao_Round, Numero_Round, ID_Partida) VALUES
(TRUE, '00:01:14', 1, 2),
(TRUE, '00:01:09', 2, 2),
(FALSE, '00:01:11', 3, 2);

-- INSERE DADOS DO ROUN MAPA ICEBOX
INSERT INTO Round (Vencedor_Round, Duracao_Round, Numero_Round, ID_Partida) VALUES
(FALSE, '00:01:18', 1, 3),
(TRUE, '00:01:22', 2, 3),
(TRUE, '00:01:12', 3, 3),
(FALSE, '00:01:16', 4, 3),
(TRUE, '00:01:17', 5, 3);

-- CONSULTAS

SELECT * FROM Rank_Jogo;
SELECT * FROM Rank_Jogo WHERE Pontuacao > 50;

SELECT * FROM Jogador;
SELECT Nome, Nivel FROM Jogador WHERE Nivel > 20;

SELECT * FROM Jogo;

SELECT * FROM Partida;
SELECT * FROM Partida WHERE Duracao_da_Partida > '00:30:00';

SELECT * FROM Round;
SELECT * FROM Round WHERE Vencedor_Round = TRUE;

SELECT * FROM Joga;
SELECT * FROM Joga WHERE Eliminacoes > 20;

-- Jogadores + rank (nível > 50)
select jogador.nome, jogador.nivel, rank_jogo.niveis_de_rank from jogador, rank_jogo where jogador.id_rank = rank_jogo.id_rank 
  and jogador.nivel > 50 order by jogador.nivel desc;

-- Partidas
select id_partida, mapa, placar from partida;

-- Jogadores por partida
select partida.mapa, jogador.nome from joga, partida, jogador where joga.id_partida = partida.id_partida
  and joga.id_jogador = jogador.id_jogador;

-- Jogadores com >20 kills + mapa
select jogador.nome, joga.eliminacoes, partida.mapa from joga, jogador, partida where joga.id_jogador = jogador.id_jogador
  and joga.id_partida = partida.id_partida
  and joga.eliminacoes > 20;

-- Quantos são Radiante
select count(*) from jogador, rank_jogo where jogador.id_rank = rank_jogo.id_rank
  and rank_jogo.niveis_de_rank = 'Radiante';

-- Jogadores Imortal ou Ascendente
select jogador.nome, rank_jogo.niveis_de_rank from jogador, rank_jogo where jogador.id_rank = rank_jogo.id_rank
  and rank_jogo.niveis_de_rank in ('Imortal', 'Ascendente') order by jogador.nome;

-- Partidas + jogadores (duração > 30m)
select partida.mapa, partida.duracao_da_partida, jogador.nome from joga, partida, jogador where joga.id_partida = partida.id_partida
  and joga.id_jogador = jogador.id_jogador
  and partida.duracao_da_partida > '00:30:00';

-- Rounds + mapa
select round.numero_round, round.vencedor_round, partida.mapa from round, partida where round.id_partida = partida.id_partida;