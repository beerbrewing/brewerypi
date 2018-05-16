"""empty message

Revision ID: 69206798fe36
Revises: 5b51435f491a
Create Date: 2018-05-15 18:59:57.545485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69206798fe36'
down_revision = '5b51435f491a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('EventFrameAttributeTemplate',
    sa.Column('EventFrameAttributeTemplateId', sa.Integer(), nullable=False),
    sa.Column('Description', sa.String(length=255), nullable=True),
    sa.Column('EventFrameTemplateId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.ForeignKeyConstraint(['EventFrameTemplateId'], ['EventFrameTemplate.EventFrameTemplateId'], name='FK__EventFrameTemplate$Have$EventFrameAttributeTemplate'),
    sa.PrimaryKeyConstraint('EventFrameAttributeTemplateId'),
    sa.UniqueConstraint('EventFrameTemplateId', 'Name', name='AK__EventFrameTemplateId__Name')
    )
    op.create_table('EventFrameAttribute',
    sa.Column('EventFrameAttributeId', sa.Integer(), nullable=False),
    sa.Column('EventFrameAttributeTemplateId', sa.Integer(), nullable=False),
    sa.Column('EventFrameId', sa.Integer(), nullable=False),
    sa.Column('TagId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['EventFrameAttributeTemplateId'], ['EventFrameAttributeTemplate.EventFrameAttributeTemplateId'], name='FK__EventFrameAttributeTemplate$Have$EventFrameAttribute'),
    sa.ForeignKeyConstraint(['EventFrameId'], ['EventFrame.EventFrameId'], name='FK__EventFrame$Have$EventFrameAttribute'),
    sa.ForeignKeyConstraint(['TagId'], ['Tag.TagId'], name='FK__Tag$Have$EventFrameAttribute'),
    sa.PrimaryKeyConstraint('EventFrameAttributeId'),
    sa.UniqueConstraint('EventFrameAttributeTemplateId', 'EventFrameId', name='AK__EventFrameAttributeTemplateId__EventFrameId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('EventFrameAttribute')
    op.drop_table('EventFrameAttributeTemplate')
    # ### end Alembic commands ###
