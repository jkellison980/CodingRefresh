class Race:
    NAME = "Uknown"
    def __init__(self, ability_bonuses=None, traits=None):
        self.ability_bonuses = ability_bonuses or {}
        self.traits = traits or []
    
    # Apply standard race features
    def apply_to_character(self, character):
        self._apply_ability_bonusses(character)
        self._apply_traits(character)
        self._on_apply(character)

    # --- Core logic shared by all races ---   
    def _apply_ability_bonuses(self, character):
        for ability, bonus in self.ability_bonuses.items():
            if ability not in character.abilities:
                raise ValueError(
                    f"Invalid ability '{ability}' in race {self.NAME}"
                )
            character.abilities[ability].base += bonus

    def _apply_traits(self, character):
        for trait in self.traits:
            character.traits[trait] = True

    # --- Hook for subclasses ---
    def _on_apply(self, character):
        pass

