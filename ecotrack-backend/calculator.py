from app import app, db
from app import ElecData, WasteData, FuelData

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Elecal': ElecData, 'Wastecal': WasteData, 'Fuelcal': FuelData}