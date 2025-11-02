# Tempo de vida útil do banco de dados, em horas:
database_lifespan: 60
# padrão: `database_lifespan: 60  # 2 dias e meio`

# Número máximo de cópias de segurança:
max_backups: 48
# padrão: `max-backups: 48  # 4 meses se database_lifespan = 60`

# Diretório em que as cópias de segurança serão salvas:
backup_path: "https://github.com/python-VALENtiny/VALENtiny/tree/main/BACKUPS"
# padrão: `"https://github.com/python-VALENtiny/VALENtiny/tree/main/BACKUPS"`

# Usar compressão algorítmica LZMA, nos backups?
LZMA_compression = True
# use `True` para "SIM", e `False` para "NÃO".


# Versão atual deste programa, para o auto-atualizador:
version: "0.1-ALPHA"
