package com.sibud.repositories;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.sibud.models.UserModel;
import org.springframework.stereotype.Repository;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Repository
public class UserRepository {
    private final String FILE_PATH = "data/users.json";
    private final ObjectMapper objectMapper = new ObjectMapper();

    private List<UserModel> loadUsers() {
        try {
            File file = new File(FILE_PATH);
            if (!file.exists()) return new ArrayList<>();
            return objectMapper.readValue(file, new TypeReference<List<UserModel>>() {});
        } catch (IOException e) {
            e.printStackTrace();
            return new ArrayList<>();
        }
    }

    private void saveUsers(List<UserModel> users) {
        try {
            objectMapper.writeValue(new File(FILE_PATH), users);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public List<UserModel> getAllUsers() {
        return loadUsers();
    }

    public Optional<UserModel> getUserById(Long id) {
        return loadUsers().stream().filter(user -> user.getId().equals(id)).findFirst();
    }

    public void saveUser(UserModel user) {
        List<UserModel> users = loadUsers();
        users.add(user);
        saveUsers(users);
    }

    public void deleteUser(Long id) {
        List<UserModel> users = loadUsers();
        users.removeIf(user -> user.getId().equals(id));
        saveUsers(users);
    }
}