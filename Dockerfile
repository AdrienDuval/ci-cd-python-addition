FROM python:3.11-slim

WORKDIR /app

# Le code applicatif et ses tests
COPY addition.py test_addition.py ./

# Par defaut, l'image execute la suite de tests
CMD ["python", "-m", "unittest", "discover", "-v"]
