package com.example.demo.domain;


public class Place {
    public String getTime_start() {
        return time_start;
    }

    public void setTime_start(String time_start) {
        this.time_start = time_start;
    }

    public String getStart_lat() {
        return start_lat;
    }

    public void setStart_lat(String start_lat) {
        this.start_lat = start_lat;
    }

    public String getStart_lon() {
        return start_lon;
    }

    public void setStart_lon(String start_lon) {
        this.start_lon = start_lon;
    }

    public String getSpend_time() {
        return spend_time;
    }

    public void setSpend_time(String spend_time) {
        this.spend_time = spend_time;
    }

    public String getTime_end() {
        return time_end;
    }

    public void setTime_end(String time_end) {
        this.time_end = time_end;
    }

    public String getEnd_lat() {
        return end_lat;
    }

    public void setEnd_lat(String end_lat) {
        this.end_lat = end_lat;
    }

    public String getEnd_lon() {
        return end_lon;
    }

    public void setEnd_lon(String end_lon) {
        this.end_lon = end_lon;
    }

    public String getEnd_sights() {
        return end_sights;
    }

    public void setEnd_sights(String end_sights) {
        this.end_sights = end_sights;
    }

    public String time_start;
    public String start_lat;
    public String start_lon;
    public String spend_time;
    public String time_end;
    public String end_lat;
    public String end_lon;
    public String end_sights;

    public Place(){ }

}
