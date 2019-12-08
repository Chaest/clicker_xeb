package fr.xebia.clickcount.repository;

import fr.xebia.clickcount.Configuration;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioSocketChannel;
import org.redisson.config.Config;
import org.redisson.Redisson;
import org.redisson.api.RedissonClient;
import org.redisson.client.RedisClient;
import org.redisson.client.RedisClientConfig;
import org.redisson.client.RedisConnection;
import org.redisson.client.RedisConnectionException;
import org.redisson.client.protocol.RedisCommands;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


import javax.inject.Inject;
import javax.inject.Singleton;

@Singleton
public class ClickRepository {

    private static final Logger log = LoggerFactory.getLogger(ClickRepository.class);

    private final RedissonClient redisClient;
    
    private final Configuration configuration;
   

    @Inject
    public ClickRepository(Configuration configuration) {
    	this.configuration = configuration;
        Config config = new Config();
        config.useSingleServer().setAddress(String.format("redis://%s:%d", configuration.redisHost, configuration.redisPort));

        redisClient = Redisson.create(config);
    }

    public String ping() {
    	RedisClient client = RedisClient.create(new RedisClientConfig().setAddress(configuration.redisHost, configuration.redisPort));
        RedisConnection conn = null;
        try {
            conn = client.connect();
            return conn.sync(RedisCommands.PING);

        } catch (RedisConnectionException e) {
            return e.getCause().getMessage();
        } finally {
            if (conn != null) {
                conn.closeAsync();
            }
        }
    }

    public long getCount() {
        log.info(">> getCount");
        return redisClient.getAtomicLong("count").get();
    }

    public long incrementAndGet() {
        log.info(">> incrementAndGet");
        return redisClient.getAtomicLong("count").incrementAndGet();
    }

}
