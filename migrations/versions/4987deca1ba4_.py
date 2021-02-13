"""empty message

Revision ID: 4987deca1ba4
Revises: f2d8c0ba9b1d
Create Date: 2021-02-11 02:09:02.540243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4987deca1ba4'
down_revision = 'f2d8c0ba9b1d'
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
