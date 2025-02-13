package com.sibud.services;

import com.sibud.models.UserModel;
import com.sibud.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    public List<UserModel> getAllUsers() {
        return userRepository.getAllUsers();
    }

    public Optional<UserModel> getUserById(Long id) {
        return userRepository.getUserById(id);
    }

    public void saveUser(UserModel user) {
        userRepository.saveUser(user);
    }

    public void deleteUser(Long id) {
        userRepository.deleteUser(id);
    }
}
