from fastapi import FastAPI, HTTPException, Request
import redis

# Initialize Redis client with cloud-hosted settings
redis_client = redis.StrictRedis(
    host='redis-12797.c292.ap-southeast-1-1.ec2.redns.redis-cloud.com',  # Cloud Redis host
    port=12797,                                                            # Cloud Redis port
    password='HmQMbJB5xUBclmV44AwiKm5cgshKz6qL',                                 # Replace with your actual password
    decode_responses=True
)

# Initialize FastAPI app
app = FastAPI()

# Set rate limit: Max 5 requests per IP per minute
RATE_LIMIT = 5
TIME_WINDOW = 60  # 60 seconds

@app.get("/data")
async def get_data(request: Request):
    ip_address = request.client.host

    # Check request count for this IP
    request_count = redis_client.get(ip_address)
    
    if request_count is None:
        # First request for this IP
        redis_client.set(ip_address, 1, ex=TIME_WINDOW)
    elif int(request_count) >= RATE_LIMIT:
        # Too many requests
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again later.")
    else:
        # Increment request count
        redis_client.incr(ip_address)

    return {"message": "Here is your data!"}

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the API!"}
