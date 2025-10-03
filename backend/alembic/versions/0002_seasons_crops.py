from alembic import op
import sqlalchemy as sa

revision = '0002_seasons_crops'
down_revision = '0001_init'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'seasons',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=50), nullable=False, unique=True),
    )
    op.create_table(
        'crops',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=80), nullable=False, unique=True),
    )
    op.create_table(
        'farm_crops',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('farm_id', sa.Integer(), sa.ForeignKey('farms.id', ondelete='CASCADE'), nullable=False),
        sa.Column('season_id', sa.Integer(), sa.ForeignKey('seasons.id', ondelete='CASCADE'), nullable=False),
        sa.Column('crop_id', sa.Integer(), sa.ForeignKey('crops.id', ondelete='CASCADE'), nullable=False),
        sa.UniqueConstraint('farm_id','season_id','crop_id', name='uq_farm_season_crop'),
    )

def downgrade():
    op.drop_table('farm_crops')
    op.drop_table('crops')
    op.drop_table('seasons')