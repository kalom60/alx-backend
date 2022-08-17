import redis, { createClient } from 'redis';

const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (error) =>
  console.log(`Redis client not connected to the server: ${error.message}`)
);

const hash_key = 'HolbertonSchools';

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.map((key, index) => {
  client.hset(hash_key, key, values[index], redis.print);
});

client.hgetall(hash_key, (err, res) => {
  console.log(res);
});
