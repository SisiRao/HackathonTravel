package com.example.demo.controller;

import com.example.demo.domain.Place;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.*;

@RestController()
@RequestMapping("/")
public class BackendController {

    private static final Logger LOG = LoggerFactory.getLogger(BackendController.class);

    public static final String HELLO_TEXT = "Hello from Spring Boot Backend!";


    @RequestMapping(path = "/hello")
    public @ResponseBody
    String sayHello() {
        LOG.info("GET called on /hello resource");
        return HELLO_TEXT;
    }

    @RequestMapping(value = "/plan", method = RequestMethod.POST)
    @ResponseBody
    public Place[] getPlan(@RequestBody String pos) {
        Place[] places = new Place[4];
        for (Place p : places) {
            p = new Place();
        }
        places = setData(places);

        return places;
    }

    private Place[] setData(Place[] places) {

        return places;
    }


//    @RequestMapping(path = "/user", method = RequestMethod.POST)
//    @ResponseStatus(HttpStatus.CREATED)
//    public @ResponseBody
//    long addNewUser (@RequestParam String firstName, @RequestParam String lastName) {
//        User user = new User(firstName, lastName);
//        userRepository.save(user);
//
//        LOG.info(user.toString() + " successfully saved into DB");
//
//        return user.getId();
//    }
//
//    @GetMapping(path="/user/{id}")
//    public @ResponseBody
//    User getUserById(@PathVariable("id") long id) {
//        LOG.info("Reading user with id " + id + " from database.");
//        return userRepository.findById(id).get();
//    }

}
