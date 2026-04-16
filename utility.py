# Utility.py a professional module for system tools
def foramt_system_report(status_data):
    """formats raw dictionary data into a professional string"""
    report = f"--- System Report ---\n"
    for key, value in status_data.items():
        report += f"{key.upper()}: {value}\n"
    return report

def calculate_uptime_percentage(days_online):
    """Calculates reliability percentage based on a 365 - day year"""
    percentage = (days_online/365)*100
    return f"{round(percentage,2)}%"