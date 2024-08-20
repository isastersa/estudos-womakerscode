import sqlite3

conexao = sqlite3.connect('/Users/isabellastersa/Desktop/Isabella/estudos-womakerscode/sql/banco.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuario(
               id INT, 
               nome VARCHAR(100), 
               endereco VARCHAR(100),
               email VARCHAR(100)
               )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS gerente(
               id INT, 
               nome VARCHAR(100), 
               endereco VARCHAR(100),
               email VARCHAR(100)
               )''')
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefone INT')

#cursor.execute("INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (1, 'Ana Silva', 'Rua A, 123', 'ana.silva@example.com', 123456789)")
#cursor.execute("INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (2, 'João Pereira', 'Rua B, 456', 'joao.pereira@example.com', 234567890)")
#cursor.execute("INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (3, 'Maria Oliveira', 'Rua C, 789', 'maria.oliveira@example.com', 345678901)")
#cursor.execute("INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (4, 'Pedro Santos', 'Rua D, 101', 'pedro.santos@example.com', 456789012)")
#cursor.execute("INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (5, 'Carlos Almeida', 'Rua E, 202', 'carlos.almeida@example.com', 567890123)")
#cursor.execute("INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (6, 'Juliana Costa', 'Rua F, 303', 'juliana.costa@example.com', 678901234)")
#cursor.execute("INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (7, 'Fernanda Martins', 'Rua G, 404', 'fernanda.martins@example.com', 789012345)")
#cursor.execute("INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (8, 'Lucas Lima', 'Rua H, 505', 'lucas.lima@example.com', 890123456)")
#cursor.execute("INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (9, 'Patrícia Ribeiro', 'Rua I, 606', 'patricia.ribeiro@example.com', 901234567)")
#cursor.execute("INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (10, 'Ricardo Ferreira', 'Rua J, 707', 'ricardo.ferreira@example.com', 123456780)")

#cursor.execute("INSERT INTO usuarios (id, nome, endereco, email) VALUES (1, 'Sofia Fernandes', 'Rua U, 1818', 'sofia.fernandes@example.com')")
#cursor.execute("INSERT INTO usuarios (id, nome, endereco, email) VALUES (2, 'Gustavo Nunes', 'Rua V, 1919', 'gustavo.nunes@example.com')")
#cursor.execute("INSERT INTO usuarios (id, nome, endereco, email) VALUES (3, 'Amanda Lima', 'Rua W, 2020', 'amanda.lima@example.com')")
#cursor.execute("INSERT INTO usuarios (id, nome, endereco, email) VALUES (4, 'Felipe Almeida', 'Rua X, 2121', 'felipe.almeida@example.com')")
#cursor.execute("INSERT INTO usuarios (id, nome, endereco, email) VALUES (5, 'Roberta Vieira', 'Rua Y, 2222', 'roberta.vieira@example.com')")
#cursor.execute("INSERT INTO usuarios (id, nome, endereco, email) VALUES (6, 'Thiago Castro', 'Rua Z, 2323', 'thiago.castro@example.com')")
#cursor.execute("INSERT INTO usuarios (id, nome, endereco, email) VALUES (7, 'Patrícia Santos', 'Rua AA, 2424', 'patricia.santos@example.com')")
#cursor.execute("INSERT INTO usuarios (id, nome, endereco, email) VALUES (8, 'Leonardo Moreira', 'Rua BB, 2525', 'leonardo.moreira@example.com')")
#cursor.execute("INSERT INTO usuarios (id, nome, endereco, email) VALUES (9, 'Simone Pereira', 'Rua CC, 2626', 'simone.pereira@example.com')")
#cursor.execute("INSERT INTO usuarios (id, nome, endereco, email) VALUES (10, 'Renan Silva', 'Rua DD, 2727', 'renan.silva@example.com')")

# JOINs
# INNER JOIN - Retorna apenas as linhas que têm correspondência em ambas as tabelas.
# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerente ON usuario.id = gerente.id')
# LEFT JOIN - Retorna todas as linhas da tabela da esquerda e as linhas correspondentes da tabela da direita; se não houver correspondência, retorna NULL para a tabela da direita.
# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerente ON usuario.id = gerente.id')
# RIGHT JOIN - Retorna todas as linhas da tabela da direita e as linhas correspondentes da tabela da esquerda; se não houver correspondência, retorna NULL para a tabela da esquerda.
# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerente ON usuario.id = gerente.id')
# FULL JOIN - Retorna todas as linhas quando há uma correspondência em uma das tabelas; se não houver correspondência, retorna NULL para as tabelas sem correspondência.
# dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerente ON usuario.id = gerente.id')


# SUB-CONSULTAS
# dados = cursos.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerente)')

dados = cursor.execute('SELECT * FROM usuario')

for usuario in dados:
    print(usuario)

conexao.commit()
conexao.close()
