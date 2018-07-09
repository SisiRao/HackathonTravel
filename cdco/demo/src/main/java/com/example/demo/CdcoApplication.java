package com.example.demo;

import com.example.demo.dao.SystemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

import javax.sql.DataSource;

@SpringBootApplication
@EnableJpaRepositories("com.example.demo.dao")
@EntityScan("com.example.demo.model")
public class CdcoApplication implements CommandLineRunner {

	@Autowired
	DataSource dataSource;

	@Autowired
	SystemRepository systemRepository;

	public static void main(String[] args) {
		SpringApplication.run(CdcoApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		System.out.println("Our DataSource is = " + dataSource);
		Iterable<com.example.demo.model.System> systemlist = systemRepository.findAll();
		for(com.example.demo.model.System systemmodel:systemlist){
			System.out.println("Here is a system: " + systemmodel.toString());
		}

	}

}
