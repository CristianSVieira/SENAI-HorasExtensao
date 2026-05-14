from app.core.security import verificar_senha, criar_token_acesso


def realizar_login_service(db, cpf: str, senha: str):
    cursor = db.cursor(dictionary=True)

    query = """
        SELECT u.id, u.nome, u.cpf, u.email, u.senha, tu.nome as tipo_usuario
        FROM usuario u
        JOIN tipo_usuario tu ON u.tipo_usuario_id = tu.id
        WHERE u.cpf = %s
    """

    cursor.execute(query, (cpf,))
    user = cursor.fetchone()

    if not user or not verificar_senha(senha, user["senha"]):
        raise HTTPException(status_code=401, detail="CPF ou senha incorretos")

    token = criar_token_acesso({
        "sub": str(user["id"]),
        "role": user["tipo_usuario"],
        "nome": user["nome"]
    })

    cursor.close()

    return {
        "access_token": token,
        "token_type": "bearer"
    }