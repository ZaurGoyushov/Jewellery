"""empty message

Revision ID: 20fbb41adb0b
Revises: 7b26abf6701d
Create Date: 2021-01-28 18:23:08.552701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20fbb41adb0b'
down_revision = '7b26abf6701d'
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