package fr.xebia.clickcount;

import javax.inject.Singleton;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

@Singleton
public class Configuration {

    public final String redisHost;
    public final int redisPort;
    public final int redisConnectionTimeout;  //milliseconds

    public Configuration() {
        redisHost = System.getenv("REDIS_HOST");
        redisPort = 6379;
        redisConnectionTimeout = 2000;
    }
}
