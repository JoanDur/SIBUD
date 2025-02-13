package com.sibud.services;

import com.sibud.models.UserModel;
import com.sibud.repositories.UserRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

public class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserService userService;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    public void testGetAllUsers() {
        UserModel user1 = new UserModel(1L, "John Doe", "john.doe@example.com", "1234567890");
        UserModel user2 = new UserModel(2L, "Jane Smith", "jane.smith@example.com", "0987654321");
        List<UserModel> users = Arrays.asList(user1, user2);

        when(userRepository.getAllUsers()).thenReturn(users);

        List<UserModel> result = userService.getAllUsers();
        assertEquals(2, result.size());
        assertEquals("John Doe", result.get(0).getName());
        assertEquals("Jane Smith", result.get(1).getName());
    }

    @Test
    public void testGetUserById() {
        UserModel user = new UserModel(1L, "John Doe", "john.doe@example.com", "1234567890");

        when(userRepository.getUserById(1L)).thenReturn(Optional.of(user));

        Optional<UserModel> result = userService.getUserById(1L);
        assertTrue(result.isPresent());
        assertEquals("John Doe", result.get().getName());
    }

    @Test
    public void testSaveUser() {
        UserModel user = new UserModel(1L, "John Doe", "john.doe@example.com", "1234567890");

        doNothing().when(userRepository).saveUser(user);
        userService.saveUser(user);

        verify(userRepository, times(1)).saveUser(user);
    }

    @Test
    public void testDeleteUser() {
        doNothing().when(userRepository).deleteUser(1L);
        userService.deleteUser(1L);

        verify(userRepository, times(1)).deleteUser(1L);
    }
}
