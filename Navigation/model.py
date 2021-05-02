import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        "*** YOUR CODE HERE ***"
        self.state_size = state_size
        self.action_size = action_size
        self.hidden_size = [78,78]
        self.model = nn.Sequential(
            nn.Linear(self.state_size, self.hidden_size[0]),
            nn.ReLU(),
            nn.Linear(self.hidden_size[0], self.hidden_size[1]),
            nn.ReLU(),
            nn.Linear(self.hidden_size[1], self.action_size)
            # nn.ReLU(),
            # nn.Softmax(dim=1))
        )

    def forward(self, state):
        """Build a network that maps state -> action values."""
        logits = self.model(state)
        return logits