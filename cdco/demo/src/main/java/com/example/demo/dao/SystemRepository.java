package com.example.demo.dao;

import com.example.demo.model.System;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SystemRepository extends CrudRepository<System,Long> {
	

}
