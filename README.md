## Instructions to Use the Vue.js and Flask Web Application

### Prerequisites

Before you start, ensure you have the following installed on your system:

* [Node.js](https://nodejs.org/) (which includes npm)
* [Python](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)
* [Virtualenv](https://pypi.org/project/virtualenv/) (optional but recommended)

### 1. Clone the Repository

First, clone the repository from GitHub to your local machine:

```
git clone <your-repo-url>
cd <your-repo-directory>
```

### 2. Set Up the Backend (Flask)

#### Create a Virtual Environment

It's a good practice to use a virtual environment to manage your project dependencies. Navigate to the backend directory and create a virtual environment:

```
cd backend
python -m venv venv
```

Activate the virtual environment:

* On Windows:

```
venv\Scripts\activate
```

* On macOS and Linux:

```
source venv/bin/activate
```

#### Install Dependencies

Install the required Python packages using `pip`:

```
pip install -r requirements.txt
```

#### Configure Environment Variables

Create a `.env` file in the `backend` directory and add your environment variables. For example:

```
API_KEY=your_api_key_here
```

#### Run the Flask Application

Start the Flask server:

```
flask run
```

The backend server should now be running at `http://127.0.0.1:5000`.

### 3. Set Up the Frontend (Vue.js)

Navigate to the frontend directory:

```
cd ../frontend
```

#### Install Dependencies

Install the required Node.js packages using npm:

```
npm install
```

#### Run the Vue.js Application

Start the Vue.js development server:

```
npm run serve
```

The frontend server should now be running at `http://localhost:8080`.

### 4. Access the Application

Open your web browser and navigate to `http://localhost:8080`. You should see the frontend of your web application.