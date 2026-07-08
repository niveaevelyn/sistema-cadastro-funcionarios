import sqlite3

def conectar():
    conexao = sqlite3.connect("funcionarios.db")
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS funcionarios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   idade INTEGER,
                   cargo TEXT,
                   salario REAL)""")
    
    conexao.commit()
    conexao.close()

def cadastrar_funcionario(nome, idade, cargo, salario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO funcionarios (nome, idade, cargo, salario) VALUES (?, ?, ?, ?)",
                   (nome, idade, cargo, salario))
    
    conexao.commit()
    conexao.close()
    print(f"✅ Funcionário {nome} cadastrado com sucesso!")

def listar_funcionarios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM funcionarios ORDER BY id")
    funcionarios = cursor.fetchall()
    conexao.close()

    if not funcionarios:
        print("\n📭 Nenhum funcionário cadastrado.")
        return
    
    print("\n" + "="*60)
    print(f"{'ID':<5} {'NOME':<20} {'IDADE':<6} {'CARGO':<15} {'SALÁRIO':<10}")
    print("="*60)
    for func in funcionarios:
        print(f"{func[0]:<5} {func[1]:<20} {func[2]:<6} {func[3]:<15} {func[4]:<10.2f}")
    print("="*60)

def buscar_funcionario(termo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""SELECT * FROM funcionarios
                   WHERE nome LIKE ? OR cargo LIKE ?
                   ORDER BY id""", (f'%{termo}%', f'%{termo}%'))
    
    funcionarios = cursor.fetchall()
    conexao.close()

    if not funcionarios:
        print(f"\n🔍 Nenhum funcionário encontrado para: {termo}")
        return
    
    print(f"\n🔍 Resultados para: {termo}")
    for func in funcionarios:
        print(f"\nID: {func[0]} | Nome: {func[1]} | Idade: {func[2]} | Cargo: {func[3]} | Salário: R${func[4]:.2f}")

def atualizar_funcionario(id, nome, idade, cargo, salario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""UPDATE funcionarios
                   SET nome = ?, idade = ?, cargo = ?, salario = ?
                   WHERE id = ?""", (nome, idade, cargo, salario, id))
    
    if cursor.rowcount > 0:
        conexao.commit()
        print(f"✅ Funcionário ID {id} atualizado com sucesso!")
    else:
        print(f"❌ Funcionário ID {id} não encontrado.")

    conexao.close()

def excluir_funcionario(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id,))

    if cursor.rowcount > 0:
        conexao.commit()
        print(f"✅ Funcionário ID {id} excluído com sucesso!")
    else:
        print(f"❌ Funcionário ID {id} não encontrado.")
    
    conexao.close()