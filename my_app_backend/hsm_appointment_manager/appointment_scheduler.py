from uuid import uuid4

def _generate_id():
    return str(uuid4())

class AppointmentScheduler:
    def __init__(self, database):
        self.database = database
        self.scheduled = False
    
    def schedule(self, attribute, context_method, execution_method):
        appointment = getattr(self, attribute)
        appointment_id = _generate_id()
        data = vars(appointment)
        data['appointment_id'] = appointment_id
        data['appointment_status'] = 'scheduled'
        columns = list(data.keys())
        values = list(data.values())
        return {"table": "appointments", "columns": columns, "values": values, "context_method": context_method, "execution_method": execution_method}
    
    def reschedule(self, attribute, update_data, context_method, execution_method):
        condition = getattr(self, attribute)
        update_dict = getattr(self, update_data)
        columns, values = [], []
        for key, value in update_dict.items():
            columns.append(key)
            values.append(value)
        return {"table": "appointments", "columns": columns, "values": values, "condition": condition, "context_method": context_method, "execution_method": execution_method}
    
    def cancel(self, attribute, context_method, execution_method):
        condition = getattr(self, attribute)
        return {"table": "appointments", "condition": condition, "context_method": context_method, "execution_method": execution_method}