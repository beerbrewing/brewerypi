"""empty message

Revision ID: 1476a62140ae
Revises: 
Create Date: 2017-12-18 20:49:51.768913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1476a62140ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Enterprise',
    sa.Column('EnterpriseId', sa.Integer(), nullable=False),
    sa.Column('Abbreviation', sa.String(length=10), nullable=False),
    sa.Column('Description', sa.String(length=255), nullable=True),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('EnterpriseId'),
    sa.UniqueConstraint('Abbreviation', name='AK__Abbreviation'),
    sa.UniqueConstraint('Name', name='AK__Name')
    )
    op.create_table('UnitOfMeasurement',
    sa.Column('UnitOfMeasurementId', sa.Integer(), nullable=False),
    sa.Column('Abbreviation', sa.String(length=15), nullable=False),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('UnitOfMeasurementId'),
    sa.UniqueConstraint('Abbreviation', 'Name', name='AK__Abbreviation__Name')
    )
    op.create_table('Lookup',
    sa.Column('LookupId', sa.Integer(), nullable=False),
    sa.Column('EnterpriseId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.ForeignKeyConstraint(['EnterpriseId'], ['Enterprise.EnterpriseId'], name='FK__Enterprise$Have$Lookup'),
    sa.PrimaryKeyConstraint('LookupId'),
    sa.UniqueConstraint('EnterpriseId', 'Name', name='AK__EnterpriseId__Name')
    )
    op.create_table('Site',
    sa.Column('SiteId', sa.Integer(), nullable=False),
    sa.Column('Abbreviation', sa.String(length=10), nullable=False),
    sa.Column('Description', sa.String(length=255), nullable=True),
    sa.Column('EnterpriseId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.ForeignKeyConstraint(['EnterpriseId'], ['Enterprise.EnterpriseId'], name='FK__Enterprise$Have$Site'),
    sa.PrimaryKeyConstraint('SiteId'),
    sa.UniqueConstraint('Abbreviation', 'EnterpriseId', name='AK__Abbreviation__EnterpriseId'),
    sa.UniqueConstraint('EnterpriseId', 'Name', name='AK__EnterpriseId__Name')
    )
    op.create_table('Area',
    sa.Column('AreaId', sa.Integer(), nullable=False),
    sa.Column('Abbreviation', sa.String(length=10), nullable=False),
    sa.Column('Description', sa.String(length=255), nullable=True),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.Column('SiteId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['SiteId'], ['Site.SiteId'], name='FK__Site$Have$Area'),
    sa.PrimaryKeyConstraint('AreaId'),
    sa.UniqueConstraint('Abbreviation', 'SiteId', name='AK__Abbreviation__SiteId'),
    sa.UniqueConstraint('Name', 'SiteId', name='AK__Name__SiteId')
    )
    op.create_table('ElementTemplate',
    sa.Column('ElementTemplateId', sa.Integer(), nullable=False),
    sa.Column('Description', sa.String(length=255), nullable=True),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.Column('SiteId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['SiteId'], ['Site.SiteId'], name='FK__Site$Have$ElementTemplate'),
    sa.PrimaryKeyConstraint('ElementTemplateId'),
    sa.UniqueConstraint('Name', 'SiteId', name='AK__Name__SiteId')
    )
    op.create_table('LookupValue',
    sa.Column('LookupValueId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.Column('Selectable', sa.Boolean(), nullable=False),
    sa.Column('LookupId', sa.Integer(), nullable=False),
    sa.Column('Value', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['LookupId'], ['Lookup.LookupId'], name='FK__Lookup$Have$LookupValue'),
    sa.PrimaryKeyConstraint('LookupValueId'),
    sa.UniqueConstraint('LookupId', 'Name', name='AK__LookupId__Name'),
    sa.UniqueConstraint('LookupId', 'Value', name='AK__LookupId__Value')
    )
    op.create_table('AttributeTemplate',
    sa.Column('AttributeTemplateId', sa.Integer(), nullable=False),
    sa.Column('Description', sa.String(length=255), nullable=True),
    sa.Column('ElementTemplateId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.ForeignKeyConstraint(['ElementTemplateId'], ['ElementTemplate.ElementTemplateId'], name='FK__ElementTemplate$Have$AttributeTemplate'),
    sa.PrimaryKeyConstraint('AttributeTemplateId'),
    sa.UniqueConstraint('ElementTemplateId', 'Name', name='AK__ElementTemplateId__Name')
    )
    op.create_table('Element',
    sa.Column('ElementId', sa.Integer(), nullable=False),
    sa.Column('Description', sa.String(length=255), nullable=True),
    sa.Column('ElementTemplateId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.ForeignKeyConstraint(['ElementTemplateId'], ['ElementTemplate.ElementTemplateId'], name='FK__ElementTemplate$Have$Element'),
    sa.PrimaryKeyConstraint('ElementId'),
    sa.UniqueConstraint('ElementTemplateId', 'Name', name='AK__ElementTemplateId__Name')
    )
    op.create_table('Tag',
    sa.Column('TagId', sa.Integer(), nullable=False),
    sa.Column('AreaId', sa.Integer(), nullable=False),
    sa.Column('Description', sa.String(length=255), nullable=True),
    sa.Column('LookupId', sa.Integer(), nullable=True),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.Column('UnitOfMeasurementId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['AreaId'], ['Area.AreaId'], name='FK__Area$Have$Tag'),
    sa.ForeignKeyConstraint(['LookupId'], ['Lookup.LookupId'], name='FK__Lookup$CanBeUsedIn$Tag'),
    sa.ForeignKeyConstraint(['UnitOfMeasurementId'], ['UnitOfMeasurement.UnitOfMeasurementId'], name='FK__UnitOfMeasurement$CanBeUsedIn$Tag'),
    sa.PrimaryKeyConstraint('TagId'),
    sa.UniqueConstraint('AreaId', 'Name', name='AK__AreaId__Name')
    )
    op.create_table('ElementAttribute',
    sa.Column('ElementAttributeId', sa.Integer(), nullable=False),
    sa.Column('AttributeTemplateId', sa.Integer(), nullable=False),
    sa.Column('ElementId', sa.Integer(), nullable=False),
    sa.Column('TagId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['AttributeTemplateId'], ['AttributeTemplate.AttributeTemplateId'], name='FK__AttributeTemplate$Have$ElementAttribute'),
    sa.ForeignKeyConstraint(['ElementId'], ['Element.ElementId'], name='FK__Element$Have$ElementAttribute'),
    sa.ForeignKeyConstraint(['TagId'], ['Tag.TagId'], name='FK__Tag$Have$ElementAttribute'),
    sa.PrimaryKeyConstraint('ElementAttributeId'),
    sa.UniqueConstraint('AttributeTemplateId', 'ElementId', name='AK__AttributeTemplateId__ElementId')
    )
    op.create_table('TagValue',
    sa.Column('TagValueId', sa.Integer(), nullable=False),
    sa.Column('TagId', sa.Integer(), nullable=False),
    sa.Column('Timestamp', sa.DateTime(), nullable=False),
    sa.Column('Value', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['TagId'], ['Tag.TagId'], name='FK__Tag$Have$TagValue'),
    sa.PrimaryKeyConstraint('TagValueId'),
    sa.UniqueConstraint('TagId', 'Timestamp', name='AK__TagId__Timestamp')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TagValue')
    op.drop_table('ElementAttribute')
    op.drop_table('Tag')
    op.drop_table('Element')
    op.drop_table('AttributeTemplate')
    op.drop_table('LookupValue')
    op.drop_table('ElementTemplate')
    op.drop_table('Area')
    op.drop_table('Site')
    op.drop_table('Lookup')
    op.drop_table('UnitOfMeasurement')
    op.drop_table('Enterprise')
    # ### end Alembic commands ###