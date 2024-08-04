"""empty message

Revision ID: e1ff5b61e539
Revises: c5bdf0db35d8
Create Date: 2024-08-05 05:52:00.264826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1ff5b61e539'
down_revision = 'c5bdf0db35d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('disbursement_detail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('disbursement_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['disbursement_id'], ['disbursement.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('disbursement_detail')
    # ### end Alembic commands ###
