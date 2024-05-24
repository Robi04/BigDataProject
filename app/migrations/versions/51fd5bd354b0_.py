"""empty message

Revision ID: 51fd5bd354b0
Revises: d1fe773b2605
Create Date: 2024-05-23 18:33:22.766330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51fd5bd354b0'
down_revision = 'd1fe773b2605'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asked_questions',
    sa.Column('asked_question_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('bool_aws', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('asked_question_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('asked_questions')
    # ### end Alembic commands ###