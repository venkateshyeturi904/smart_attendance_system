package project.attendancebackend.controller;



import java.io.IOException;

import javax.print.attribute.standard.Media;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping(path = "/api")
public class ImageController {

    @Autowired
    private RestTemplate restTemplate;

    @PostMapping(path = "/uploadImage")
    public ResponseEntity<String> uploadImage(@RequestParam("image") MultipartFile file) throws IOException{

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.MULTIPART_FORM_DATA);

        HttpEntity<byte[]> requestEntity = new HttpEntity<>(file.getBytes(),headers);
        // added throws something here through suggestion
        ResponseEntity<String> response = restTemplate.postForEntity("http://localhost:5000/predict_roll_numbers", requestEntity, String.class);

        return response;
    }


    // @GetMapping("/getMessage")
    // public String get(){
    //     return "Hello";
    // }
}
