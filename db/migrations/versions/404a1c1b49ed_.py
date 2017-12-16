"""empty message

Revision ID: 404a1c1b49ed
Revises: ee9cffa206dc
Create Date: 2017-12-16 10:57:53.849799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '404a1c1b49ed'
down_revision = 'ee9cffa206dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('LookupValue', sa.Column('Selectable', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('LookupValue', 'Selectable')
    # ### end Alembic commands ###