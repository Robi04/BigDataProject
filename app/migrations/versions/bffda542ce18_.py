"""empty message

Revision ID: bffda542ce18
Revises: 8d7c8f13ae50
Create Date: 2024-05-23 16:04:11.972494

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bffda542ce18'
down_revision = '8d7c8f13ae50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=255), nullable=False),
    sa.Column('aws1', sa.String(length=255), nullable=True),
    sa.Column('aws2', sa.String(length=255), nullable=False),
    sa.Column('aws3', sa.String(length=255), nullable=False),
    sa.Column('aws4', sa.String(length=255), nullable=False),
    sa.Column('correct_aws', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('question_id')
    )
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('questions')
    # ### end Alembic commands ###