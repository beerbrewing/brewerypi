"""Event Frame Template Views.

Revision ID: 8a8c98940433
Revises: 693d24be14f4
Create Date: 2020-01-02 12:41:15.349317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a8c98940433'
down_revision = '693d24be14f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('EventFrameTemplateView',
    sa.Column('EventFrameTemplateViewId', sa.Integer(), nullable=False),
    sa.Column('Default', sa.Boolean(), nullable=False),
    sa.Column('Description', sa.String(length=255), nullable=True),
    sa.Column('EventFrameTemplateId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.ForeignKeyConstraint(['EventFrameTemplateId'], ['EventFrameTemplate.EventFrameTemplateId'], name='FK__EventFrameTemplate$Have$EventFrameTemplateView'),
    sa.PrimaryKeyConstraint('EventFrameTemplateViewId'),
    sa.UniqueConstraint('EventFrameTemplateId', 'Name', name='AK__EventFrameTemplateId_Name')
    )
    op.create_table('EventFrameAttributeTemplateEventFrameTemplateView',
    sa.Column('EventFrameAttributeTemplateEventFrameTemplateViewId', sa.Integer(), nullable=False),
    sa.Column('EventFrameAttributeTemplateId', sa.Integer(), nullable=False),
    sa.Column('EventFrameTemplateViewId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['EventFrameAttributeTemplateId'], ['EventFrameAttributeTemplate.EventFrameAttributeTemplateId'], name='FK__EFAT$Have$EventFrameAttributeTemplateEventFrameTemplateView'),
    sa.ForeignKeyConstraint(['EventFrameTemplateViewId'], ['EventFrameTemplateView.EventFrameTemplateViewId'], name='FK__EFTV$Have$EventFrameAttributeTemplateEventFrameTemplateView'),
    sa.PrimaryKeyConstraint('EventFrameAttributeTemplateEventFrameTemplateViewId'),
    sa.UniqueConstraint('EventFrameAttributeTemplateId', 'EventFrameTemplateViewId', name='AK__EventFrameAttributeTemplateId__EventFrameTemplateViewId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('EventFrameAttributeTemplateEventFrameTemplateView')
    op.drop_table('EventFrameTemplateView')
    # ### end Alembic commands ###