############################################
#                                          #
#  CONFIGURAÇÕES DA MANUTENÇÃO PROGRAMADA  #
#                                          #
############################################

# Tempo de vida útil do banco de dados, em horas:
database_lifespan: 8
# padrão: `database_lifespan: 8`

# Número máximo de cópias de segurança:
max_backups: 360
# padrão: `max-backups: 360  # 4 meses se database_lifespan = 8`

# Diretório em que as cópias de segurança serão salvas:
backup_path: "https://github.com/python-VALENtiny/VALENtiny/tree/main/BACKUPS"
# padrão: `"https://github.com/python-VALENtiny/VALENtiny/tree/main/BACKUPS"`

# Usar compressão algorítmica LZMA, nos backups?
LZMA_compression = False
# use `True` para "SIM", e `False` para "NÃO".


######################
#                    #
#  AUTO-Atualizador  #
#                    #
######################

# Versão atual deste programa:
version: "0.6-ALPHA"
# Diretório da nova versão:
new_version: "https://github.com/Felipe-Valentin/VALENware/releases/download/VALENtiny__v0.6-GAMA/Windows64_VALENtiny-Maintainer.exe"
