import os

description="""Example Pmake file"""


class Pfunc:
  pmake_vars={}
  def vars():
    print(Pfunc.pmake_vars)
  def all():
    """Runs automatically when no arguments are entered"""
    print("Hello World")