"""empty message

Revision ID: f2d8c0ba9b1d
Revises: 874be8d8b9bc
Create Date: 2021-02-11 02:06:50.467185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2d8c0ba9b1d'
down_revision = '874be8d8b9bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('brand_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'products', 'brand', ['brand_id'], ['Brand_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'brand_id')
    # ### end Alembic commands ###
