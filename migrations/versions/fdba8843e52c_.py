"""empty message

Revision ID: fdba8843e52c
Revises: 105808de517f
Create Date: 2021-01-27 01:10:58.641272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdba8843e52c'
down_revision = '105808de517f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'products', 'category', ['cat_id'], ['Category_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    # ### end Alembic commands ###