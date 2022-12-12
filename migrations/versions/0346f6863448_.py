"""empty message

Revision ID: 0346f6863448
Revises: 
Create Date: 2022-12-12 01:54:19.441910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0346f6863448'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('BestTemperatureBeers',
    sa.Column('id_best_beer_temperature', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('style_beer', sa.String(length=30), nullable=True),
    sa.Column('min_best_temperature', sa.Integer(), nullable=True),
    sa.Column('max_best_temperature', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id_best_beer_temperature'),
    sa.UniqueConstraint('id_best_beer_temperature')
    )
    op.create_table('Beers',
    sa.Column('id_beer', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('style_beer', sa.String(length=30), nullable=True),
    sa.Column('id_best_beer_temperature', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['id_best_beer_temperature'], ['BestTemperatureBeers.id_best_beer_temperature'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_beer'),
    sa.UniqueConstraint('id_beer')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Beers')
    op.drop_table('BestTemperatureBeers')
    # ### end Alembic commands ###