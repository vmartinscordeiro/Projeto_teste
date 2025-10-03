from alembic import op
import sqlalchemy as sa

revision = '0001_init'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'producers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('cpf_cnpj', sa.String(length=14), nullable=False),
        sa.Column('name', sa.String(length=200), nullable=False),
    )
    op.create_index('ix_producers_cpf_cnpj', 'producers', ['cpf_cnpj'], unique=True)

    op.create_table(
        'farms',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('producer_id', sa.Integer(), sa.ForeignKey('producers.id', ondelete='CASCADE'), nullable=False),
        sa.Column('name', sa.String(length=200), nullable=False),
        sa.Column('city', sa.String(length=120)),
        sa.Column('state', sa.String(length=2)),
        sa.Column('area_total', sa.Numeric(14, 2), nullable=False),
        sa.Column('area_agricultavel', sa.Numeric(14, 2), nullable=False),
        sa.Column('area_vegetacao', sa.Numeric(14, 2), nullable=False),
        sa.CheckConstraint('area_agricultavel + area_vegetacao <= area_total', name='ck_farm_areas_validas'),
    )

def downgrade():
    op.drop_table('farms')
    op.drop_index('ix_producers_cpf_cnpj', table_name='producers')
    op.drop_table('producers')