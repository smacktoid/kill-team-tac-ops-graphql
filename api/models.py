from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from app import db

Base = declarative_base()


class KillTeam(db.Model):
    __tablename__ = "kill_team"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    archetypes = relationship('Archetype', secondary='kill_team_archetypes')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Archetype(db.Model):
    __tablename__ = "archetype"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class KillTeamArchetypes(db.Model):
    __tablename__ = "kill_team_archetypes"
    kill_team_id = Column(Integer, ForeignKey('kill_team.id'), primary_key=True)
    archetype_id = Column(Integer, ForeignKey('archetype.id'), primary_key=True)


class TacOp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    archetype_id = db.Column(db.Integer, db.ForeignKey("archetype.id"))
    kill_team_id = db.Column(db.Integer, db.ForeignKey("kill_team.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "archetype_id": self.archetype_id,
            "kill_team_id": self.kill_team_id
        }
