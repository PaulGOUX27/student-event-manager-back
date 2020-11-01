From https://github.com/tko22/flask-boilerplate

# Requirements
- Docker

# Run the back-end
Only the first time
```
docker-compose build
```

To run the back-end
```
docker-compose up
```

Enter interact with models
```
docker-compose exec app bash
python3
from api import create_app
from api.models import db, EventCategory, Event, Person
from datetime import datetime
app = create_app()
app.app_context().push()
```