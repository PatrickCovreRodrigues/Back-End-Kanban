from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from fast_zero.models import table_registry
from fast_zero.settings import Settings

# Configuração do Alembic
config = context.config
config.set_main_option('sqlalchemy.url', Settings().DATABASE_URL)

# Configuração de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadados para suporte a autogenerate
target_metadata = table_registry.metadata


def run_migrations_offline() -> None:
    """Executa as migrações em modo 'offline'.

    Configura o contexto apenas com uma URL, sem criar um Engine.
    Chamadas a context.execute() emitem os comandos diretamente.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa as migrações em modo 'online'.

    Cria um Engine e associa a conexão ao contexto.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
