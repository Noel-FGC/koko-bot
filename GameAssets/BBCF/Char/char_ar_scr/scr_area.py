@State
def EMB_AR():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_AR.DIG', '')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4278190335, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 19)

@State
def EMB_AR_OD():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_AR.DIG', '')
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294967295, 10)
    sprite('null', 10)
    ColorTransition(4286625023, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 10)
    ColorTransition(4278223103, 10)
    sprite('null', 19)

@State
def EMB_AR_AH():

    def upon_IMMEDIATE():
        FaceLeft()
        AddY(240000)
        IgnoreScreenfreeze(1)
        Visibility(1)
        Eff3DEffect('ef_emb_AR.DIG', '')
        PaletteIndex(7)
        ColorFromPaletteIndex(1)
        RenderLayer(5)
    sprite('null', 10)
    ColorForTransition(4278190080)
    ColorTransition(4294901760, 10)
    sprite('null', 10)
    ColorTransition(4294912040, 10)
    sprite('null', 10)
    ColorTransition(4294948020, 10)
    sprite('null', 10)
    ColorTransition(4294901760, 10)
    sprite('null', 19)

@State
def aref_droplet():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_down_droplet', 0)

@State
def aref_dropletL():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_dropletL', 0)

@State
def aref_dropletR():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_dropletR', 0)

@State
def aref_moveL():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_move', 0)

@State
def aref_moveR():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleRotationAngle(180000)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_move', 0)

@State
def aref_moveUP():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleRotationAngle(270000)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_move', 0)

@State
def aref_moveDOWN():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleRotationAngle(90000)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_move', 0)

@State
def aref_moveUP_R():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleRotationAngle(225000)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_move', 0)

@State
def aref_moveDOWN_R():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleRotationAngle(135000)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_move', 0)

@State
def aref_moveUP_L():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleRotationAngle(315000)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_move', 0)

@State
def aref_moveDOWN_L():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleRotationAngle(45000)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_move', 0)

@State
def aref_rotation():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_rotation', 0)

@State
def aref_damage():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_damage', 0)

@State
def aref_crash():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_crash', 0)

@State
def aref_burst():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_burst', 0)

@State
def aref_bubble():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_bubble', 0)

@State
def aref_ar201():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_ar201', 0)

@State
def vraref_ar213():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(4, 5, 6)
    CallCustomizableParticle('aref_ar213', 0)

@State
def aref_D_aura():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(7, 7, 7)
    CallCustomizableParticle('aref_D_aura', 0)

@State
def AST_AuraPtc():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AddY(220000)
    sprite('null', 2)
    CreateParticle('aref_450start', -1)

@State
def AST_AuraPtcDel():

    def upon_IMMEDIATE():
        E0EAEffectPosition(3)
        AddY(220000)
    sprite('null', 3)
    CreateParticle('aref_450del', -1)
    sprite('null', 3)
    CreateParticle('aref_450del', -1)
    sprite('null', 3)
    CreateParticle('aref_450del', -1)

@State
def shotairD_born():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        BlendMode_Normal()
    sprite('ar400_14', 3)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    sprite('ar400_15', 3)
    sprite('ar400_16', 3)
    CreateObject('aref_rotation', 0)
    CommonSE('016_explode_0')
    CommonSE('012_stab_middle')

@State
def aref_ar400_A():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        BlendMode_Normal()
        FaceLeft()
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)
        sendToLabelUpon(54, 1)
        sendToLabelUpon(32, 1)
        ContinueState(900)
        AttackDirection(1)
        EndAttack()

        def upon_FRAME_STEP():
            if (SLOT_98 < 212500):
                if (not SLOT_8):
                    if (not SLOT_110):
                        Unknown23149(20)
                    if SLOT_110:
                        Unknown23149(40)
                if SLOT_4:
                    clearUponHandler(3)
                    clearUponHandler(32)
                    sendToLabel(1)
        sendToLabelUpon(53, 1)
    sprite('null', 9)
    PaletteIndex(1)
    ParticleColorFromPalette(1, 2, 3)
    CallPrivateEffect('aref_ar400_A')
    Visibility(1)
    loopRest()
    label(10)
    sprite('vraref400_01', 1)
    CopyFromRightToLeft(23, 2, 51, 22, 2, 22)
    PrivateFunction(1, 2, 22, 2, 51, 2, 51)
    PrivateFunction(3, 2, 51, 0, 100, 2, 12)
    CopyFromRightToLeft(23, 2, 52, 22, 2, 23)
    PrivateFunction(1, 2, 23, 2, 52, 2, 52)
    PrivateFunction(0, 2, 52, 0, -200000, 2, 52)
    PrivateFunction(3, 2, 52, 0, -50, 2, 13)
    loopRest()
    GotoIf0(1, 2, 21)
    gotoLabel(10)
    label(1)
    clearUponHandler(54)
    clearUponHandler(32)
    clearUponHandler(3)
    sprite('null', 30)
    BlendMode_Normal()
    ConstantAlphaModifier(-20)
    SetScaleSpeed(100)
    CreateObject('aref_hit_insect', -1)

@State
def aref_ar400_B():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        BlendMode_Normal()
        FaceLeft()
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)
        sendToLabelUpon(54, 1)
        sendToLabelUpon(32, 1)
        ContinueState(900)
        AttackDirection(1)
        EndAttack()

        def upon_FRAME_STEP():
            if (SLOT_98 < 222500):
                if (not SLOT_8):
                    if (not SLOT_110):
                        Unknown23149(40)
                    if SLOT_110:
                        Unknown23149(80)
                if SLOT_4:
                    clearUponHandler(3)
                    clearUponHandler(32)
                    sendToLabel(1)
        sendToLabelUpon(53, 1)
    sprite('null', 9)
    PaletteIndex(1)
    ParticleColorFromPalette(1, 2, 3)
    CallPrivateEffect('aref_ar400_B')
    Visibility(1)
    loopRest()
    label(10)
    sprite('vraref400_00', 1)
    CopyFromRightToLeft(23, 2, 51, 3, 2, 22)
    PrivateFunction(1, 2, 22, 2, 51, 2, 51)
    PrivateFunction(3, 2, 51, 0, 50, 2, 12)
    CopyFromRightToLeft(23, 2, 52, 3, 2, 23)
    PrivateFunction(1, 2, 23, 2, 52, 2, 52)
    PrivateFunction(0, 2, 52, 0, -180000, 2, 52)
    PrivateFunction(3, 2, 52, 0, -50, 2, 13)
    loopRest()
    GotoIf0(1, 2, 21)
    gotoLabel(10)
    label(1)
    clearUponHandler(54)
    clearUponHandler(32)
    clearUponHandler(3)
    sprite('null', 30)
    BlendMode_Normal()
    ConstantAlphaModifier(-20)
    SetScaleSpeed(100)
    CreateObject('aref_hit_insect', -1)

@State
def aref_ar400_C():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        BlendMode_Normal()
        FaceLeft()
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)
        sendToLabelUpon(54, 1)
        sendToLabelUpon(32, 1)
        ContinueState(900)
        AttackDirection(1)
        EndAttack()

        def upon_FRAME_STEP():
            if (SLOT_98 < 212500):
                if (not SLOT_8):
                    if (not SLOT_110):
                        Unknown23149(60)
                    if SLOT_110:
                        Unknown23149(120)
                if SLOT_4:
                    clearUponHandler(3)
                    clearUponHandler(32)
                    sendToLabel(1)
            if (SLOT_19 < 50000):
                SetActionMark(1)
        sendToLabelUpon(53, 1)
    sprite('null', 25)
    PaletteIndex(1)
    ParticleColorFromPalette(1, 2, 3)
    CallPrivateEffect('aref_ar400_C')
    Visibility(1)
    CopyFromRightToLeft(23, 2, 51, 22, 2, 22)
    PrivateFunction(1, 2, 22, 2, 51, 2, 51)
    PrivateFunction(3, 2, 51, 0, 60, 2, 12)
    SLOT_52 = 135000
    PrivateFunction(1, 2, 23, 2, 52, 2, 52)
    PrivateFunction(0, 2, 52, 0, -480000, 2, 52)
    PrivateFunction(3, 2, 52, 0, -95, 2, 13)
    loopRest()
    label(10)
    sprite('vraref400_00', 1)
    CopyFromRightToLeft(23, 2, 51, 22, 2, 22)
    PrivateFunction(1, 2, 22, 2, 51, 2, 51)
    if SLOT_2:
        PrivateFunction(3, 2, 51, 0, 25, 2, 12)
    else:
        PrivateFunction(3, 2, 51, 0, 100, 2, 12)
    SLOT_52 = 135000
    PrivateFunction(1, 2, 23, 2, 52, 2, 52)
    PrivateFunction(0, 2, 52, 0, -480000, 2, 52)
    PrivateFunction(3, 2, 52, 0, -30, 2, 13)
    loopRest()
    GotoIf0(1, 2, 21)
    gotoLabel(10)
    label(1)
    clearUponHandler(54)
    clearUponHandler(32)
    clearUponHandler(3)
    sprite('null', 30)
    BlendMode_Normal()
    ConstantAlphaModifier(-20)
    SetScaleSpeed(100)
    CreateObject('aref_hit_insect', -1)

@State
def aref_hit_insect():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_hit_insect', 0)

@State
def aref_ar402_A():
    sprite('null', 1)
    PaletteIndex(0)
    E0EAEffectPosition(3)
    ParticleRotationAngle(315000)
    ParticleColorFromPalette(47, 111, 159)
    CallCustomizableParticle('aref_ar402', 0)

@State
def aref_ar402_B():
    sprite('null', 1)
    PaletteIndex(0)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(47, 111, 159)
    CallCustomizableParticle('aref_ar402', 0)

@State
def aref_ar402_C():
    sprite('null', 1)
    PaletteIndex(0)
    E0EAEffectPosition(3)
    ParticleRotationAngle(225000)
    ParticleColorFromPalette(47, 111, 159)
    CallCustomizableParticle('aref_ar402', 0)

@State
def aref_ar300():
    sprite('null', 1)
    PaletteIndex(1)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(1, 2, 3)
    CallCustomizableParticle('aref_ar300', 0)

@State
def aref_ar430():
    sprite('null', 1)
    PaletteIndex(0)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(47, 111, 159)
    CallCustomizableParticle('aref_ar430', 0)

@State
def aref_ar430_eff():
    sprite('null', 1)
    PaletteIndex(0)
    E0EAEffectPosition(3)
    ParticleColorFromPalette(47, 111, 159)
    CallCustomizableParticle('aref_ar430_eff', 0)

@State
def shot_air_Insect():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        BlendMode_Normal()
        AttackLevel_(3)
        Damage(640)
        AttackP1(90)
        AttackP2(79)
        AirUntechableTime(23)
        AirPushbackY(-10000)
        HitAirUnblockable(3)
        MoveAttributes(0, 0, 0, 1, 0)
        Hitstop(3)
        DamageEffect(2, 'Bughit')
        sendToLabelUpon(10, 1)
        sendToLabelUpon(44, 1)
        sendToLabelUpon(2, 1)
        sendToLabelUpon(32, 1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            if (not SLOT_8):
                if (not SLOT_110):
                    Curse(1500, 750)
                if SLOT_110:
                    Curse(3000, 1500)
        WallCollisionDetection(1)
    sprite('null', 2)
    sprite('vraref213_00', 4)
    Size(1000)
    AddX(696000)
    AbsoluteY(560000)
    sprite('vraref213_01', 4)
    sprite('vraref213_02', 3)
    CommonSE('022_magiccircle_c')
    sprite('vraref213_03', 3)
    sprite('vraref213_04', 3)
    sprite('vraref213_05', 3)
    sprite('vraref213_06', 5)
    physicsYImpulse(-900)
    setGravity(40)
    SetAcceleration(450)
    label(0)
    sprite('vraref213_08', 5)
    sprite('vraref213_09', 6)
    SetAcceleration(0)
    sprite('vraref213_08', 5)
    SetAcceleration(-900)
    sprite('vraref213_06', 5)
    sprite('vraref213_07', 6)
    SetAcceleration(0)
    sprite('vraref213_06', 5)
    SetAcceleration(900)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(2)
    clearUponHandler(10)
    clearUponHandler(44)
    clearUponHandler(32)
    sprite('vraref213_10', 4)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    SetAcceleration(0)
    CommonSE('012_stab_fast')
    sprite('vraref213_11', 4)
    CreateObject('vraref_ar213', 0)
    sprite('vraref213_12', 4)

@State
def shot_sit_Insect():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        BlendMode_Normal()
        AttackLevel_(3)
        Damage(640)
        AttackP2(79)
        AirUntechableTime(27)
        Hitstop(3)
        AttackDirection(4)
        MoveAttributes(0, 0, 0, 1, 0)
        DamageEffect(2, 'Bughit')
        AttackOff()

        def upon_OPPONENT_HIT_OR_BLOCK():
            if (not SLOT_8):
                if (not SLOT_110):
                    Curse(1500, 750)
                if SLOT_110:
                    Curse(3000, 1500)
        CancelIfPlayerHit(3)
        sendToLabelUpon(2, 1)
        physicsXImpulse(54000)
        physicsYImpulse(-21000)

        def upon_36():
            physicsXImpulse(27000)

        def upon_38():
            physicsXImpulse(81000)
    sprite('vraref233_00', 32767)
    label(1)
    sprite('vraref233_01', 2)
    EndMomentum(1)
    ForceFaceSprite()
    sprite('vraref233_02', 2)
    sprite('vraref233_03', 2)
    sprite('vraref233_04', 2)
    sprite('vraref233_05', 2)
    PrivateSE('arse_08')
    CreateObject('aref_rotation', 0)
    sprite('vraref233_06', 3)
    RefreshMultihit()
    sprite('vraref233_07', 3)
    sprite('vraref233_08', 3)
    sprite('vraref233_09', 3)
    CreateObject('aref_droplet', 0)
    sprite('vraref233_10', 3)
    sprite('vraref233_11', 3)
    sprite('vraref233_12', 3)

@State
def shot_ground_Insect():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        BlendMode_Normal()
        AttackLevel_(3)
        Damage(640)
        AttackP1(80)
        AttackP2(79)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(38)
        AirPushbackX(-12000)
        AirPushbackY(37750)
        PushbackX(-18000)
        Hitstop(0)
        EnemyHitstopAddition(3, 0, 2)
        MoveAttributes(0, 0, 0, 1, 0)
        DamageEffect(2, 'Bughit')

        def upon_OPPONENT_HIT_OR_BLOCK():
            PassbackAddActionMarkToFunction('NmlAtkAIR5D', 32)
            if (not SLOT_8):
                if (not SLOT_110):
                    Curse(1500, 750)
                if SLOT_110:
                    Curse(3000, 1500)
        WallCollisionDetection(1)

        def upon_33():
            AddX(820000)

        def upon_34():
            AddX(420000)

        def upon_35():
            AirPushbackX(6000)
            PushbackX(18000)
            AttackDirection(1)
            AddX(-320000)
            Flip()

        def upon_36():
            AirPushbackX(6000)
            PushbackX(18000)
            AddX(-640000)
            AttackDirection(1)
            Flip()

        def upon_37():
            NoAttackDuringAction(1)
    sprite('vraref253_00', 3)
    AddX(320000)
    AbsoluteY(0)
    Size(1000)
    sprite('vraref253_01', 3)
    sprite('vraref253_02', 3)
    sprite('vraref253_00', 3)
    sprite('vraref253_01', 3)
    sprite('vraref253_04', 3)
    CreateObject('aref_droplet', 0)
    sprite('vraref253_05', 3)
    PrivateSE('arse_08')
    PrivateSE('arse_05')
    sprite('vraref253_06', 3)
    sprite('vraref253_07', 6)
    sprite('vraref253_08', 3)
    sprite('vraref253_09', 3)
    CreateObject('aref_droplet', 0)
    sprite('vraref253_10', 3)
    sprite('vraref253_11', 3)
    sprite('vraref253_12', 3)

@State
def Bughit():
    sprite('null', -1)
    CreateParticle('aref_bughit', 0)
    CommonSE('020_blood_1')

@State
def ar430_wave():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        AbsoluteY(0)
        sendToLabelUpon(44, 9)
    sprite('vraref430_00', 4)
    CameraControlEnable(1)
    Size(1000)
    AbsoluteY(0)
    CreateObject('aref_droplet', 0)
    CreateObject('aref_ar430', -1)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_deep')
    sprite('vraref430_01', 3)
    sprite('vraref430_02', 3)
    sprite('vraref430_03', 3)
    sprite('vraref430_04', 3)
    sprite('vraref430_02', 3)
    CameraControlEnable(0)
    sprite('vraref430_03', 3)
    sprite('vraref430_02', 3)
    CallCustomizableParticle('aref_ar430_hit', -1)
    CreateObject('aref_ar430_eff', -1)
    CreateObject('ar430_Warm', 2)
    CreateObject('ar430_Warm_Atk', 6)
    PrivateSE('arse_21')
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_02', 3)
    CreateObject('ar430_Warm_Atk', 4)
    CreateObject('ar430_Warm', 8)
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm', 1)
    CreateObject('ar430_Warm_Atk', 5)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk', 3)
    CreateObject('ar430_Warm', 7)
    sprite('vraref430_04', 3)
    CreateObject('ar430_Warm', 2)
    CreateObject('ar430_Warm_Atk', 6)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_04', 3)
    CreateObject('ar430_Warm_Atk', 4)
    CreateObject('ar430_Warm', 8)
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm', 1)
    CreateObject('ar430_Warm_Atk', 5)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk', 3)
    CreateObject('ar430_Warm', 7)
    sprite('vraref430_02', 3)
    CreateObject('ar430_Warm', 2)
    CreateObject('ar430_Warm_Atk', 6)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_02', 3)
    CreateObject('ar430_Warm_Atk', 4)
    CreateObject('ar430_Warm', 8)
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm', 1)
    CreateObject('ar430_Warm_Atk', 5)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk', 3)
    CreateObject('ar430_Warm', 7)
    sprite('vraref430_04', 3)
    CreateObject('ar430_Warm', 2)
    CreateObject('ar430_Warm_Atk', 6)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_04', 3)
    CreateObject('ar430_Warm_Atk', 4)
    CreateObject('ar430_Warm', 8)
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm', 1)
    CreateObject('ar430_Warm_Atk', 5)
    PrivateSE('arse_21')
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk', 3)
    CreateObject('ar430_Warm', 7)
    sprite('vraref430_02', 3)
    CreateObject('ar430_Warm', 2)
    CreateObject('ar430_Warm_Atk', 6)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_02', 3)
    CreateObject('ar430_Warm_Atk', 4)
    CreateObject('ar430_Warm', 8)
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm', 1)
    CreateObject('ar430_Warm_Atk', 5)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk', 3)
    CreateObject('ar430_Warm', 7)
    sprite('vraref430_04', 3)
    CreateObject('ar430_Warm', 2)
    CreateObject('ar430_Warm_Atk', 6)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_04', 3)
    CreateObject('ar430_Warm_Atk', 4)
    CreateObject('ar430_Warm', 8)
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm', 1)
    CreateObject('ar430_Warm_Atk', 5)
    PrivateSE('arse_21')
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk', 3)
    CreateObject('ar430_Warm', 7)
    label(9)
    sprite('vraref430_02', 3)
    clearUponHandler(44)
    ConstantAlphaModifier(-10)
    sprite('vraref430_03', 3)
    sprite('vraref430_04', 3)
    sprite('vraref430_02', 3)
    sprite('vraref430_03', 3)
    sprite('vraref430_04', 3)

@State
def ar430_wave_OD():

    def upon_IMMEDIATE():
        TeleportToObject(22)
        AbsoluteY(0)
        sendToLabelUpon(44, 9)
    sprite('vraref430_00', 4)
    CameraControlEnable(1)
    Size(1000)
    AbsoluteY(0)
    CreateObject('aref_droplet', 0)
    CreateObject('aref_ar430', -1)
    CommonSE('012_stab_middle')
    CommonSE('012_stab_deep')
    sprite('vraref430_01', 3)
    sprite('vraref430_02', 3)
    sprite('vraref430_03', 3)
    sprite('vraref430_04', 3)
    sprite('vraref430_02', 3)
    CameraControlEnable(0)
    sprite('vraref430_03', 3)
    sprite('vraref430_02', 3)
    CallCustomizableParticle('aref_ar430_hit', -1)
    CreateObject('aref_ar430_eff', -1)
    CreateObject('ar430_Warm_Atk_OD', 2)
    CreateObject('ar430_Warm_Atk_OD', 6)
    PrivateSE('arse_21')
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_02', 3)
    CreateObject('ar430_Warm_Atk_OD', 4)
    CreateObject('ar430_Warm_Atk_OD', 8)
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk_OD', 1)
    CreateObject('ar430_Warm_Atk_OD', 5)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk_OD', 3)
    CreateObject('ar430_Warm_Atk_OD', 7)
    sprite('vraref430_04', 3)
    CreateObject('ar430_Warm_Atk_OD', 2)
    CreateObject('ar430_Warm_Atk_OD', 6)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_04', 3)
    CreateObject('ar430_Warm_Atk_OD', 4)
    CreateObject('ar430_Warm_Atk_OD', 8)
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk_OD', 1)
    CreateObject('ar430_Warm_Atk_OD', 5)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk_OD', 3)
    CreateObject('ar430_Warm_Atk_OD', 7)
    sprite('vraref430_02', 3)
    CreateObject('ar430_Warm_Atk_OD', 2)
    CreateObject('ar430_Warm_Atk_OD', 6)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_02', 3)
    CreateObject('ar430_Warm_Atk_OD', 4)
    CreateObject('ar430_Warm_Atk_OD', 8)
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk_OD', 1)
    CreateObject('ar430_Warm_Atk_OD', 5)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk_OD', 3)
    CreateObject('ar430_Warm_Atk_OD', 7)
    sprite('vraref430_04', 3)
    CreateObject('ar430_Warm_Atk_OD', 2)
    CreateObject('ar430_Warm_Atk_OD', 6)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_04', 3)
    CreateObject('ar430_Warm_Atk_OD', 4)
    CreateObject('ar430_Warm_Atk_OD', 8)
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk_OD', 1)
    CreateObject('ar430_Warm_Atk_OD', 5)
    PrivateSE('arse_21')
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk_OD', 3)
    CreateObject('ar430_Warm_Atk_OD', 7)
    sprite('vraref430_02', 3)
    CreateObject('ar430_Warm_Atk_OD', 2)
    CreateObject('ar430_Warm_Atk_OD', 6)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_02', 3)
    CreateObject('ar430_Warm_Atk_OD', 4)
    CreateObject('ar430_Warm_Atk_OD', 8)
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk_OD', 1)
    CreateObject('ar430_Warm_Atk_OD', 5)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk_OD', 3)
    CreateObject('ar430_Warm_Atk_OD', 7)
    sprite('vraref430_04', 3)
    CreateObject('ar430_Warm_Atk_OD', 2)
    CreateObject('ar430_Warm_Atk_OD', 6)
    PrivateSE('arse_21')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_04', 3)
    CreateObject('ar430_Warm_Atk_OD', 4)
    CreateObject('ar430_Warm_Atk_OD', 8)
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk_OD', 1)
    CreateObject('ar430_Warm_Atk_OD', 5)
    PrivateSE('arse_21')
    CommonSE('019_quake_0')
    CommonSE('019_quake_1')
    CommonSE('007_swing_knife_2')
    sprite('vraref430_03', 3)
    CreateObject('ar430_Warm_Atk_OD', 3)
    CreateObject('ar430_Warm_Atk_OD', 7)
    label(9)
    sprite('vraref430_02', 3)
    clearUponHandler(44)
    ConstantAlphaModifier(-10)
    sprite('vraref430_03', 3)
    sprite('vraref430_04', 3)
    sprite('vraref430_02', 3)
    sprite('vraref430_03', 3)
    sprite('vraref430_04', 3)

@State
def ar430_Warm_Atk():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(2)
        Damage(160)
        MinimumDamage(10)
        AttackP2(60)
        SingleProration(1)
        PushbackX(-6000)
        Hitstop(0)
        EnemyHitstopAddition(0, 2, 2)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(-2000)
        AirPushbackY(4000)
        AirUntechableTime(60)
        HitsparkSize(400)
        ReduceHitEffects(1)
        StarterRating(2)
        DamageEffect(2, 'Bughit')
        AttackDirection(4)

        def upon_OPPONENT_HIT_OR_BLOCK():
            if (not SLOT_8):
                Curse(500, 150)
        VoodooDamageMultiplier(2)
        BlendMode_Normal()
        ContinueState(30)

        def upon_44():
            AttackOff()

        def upon_FRAME_STEP():
            if (not SLOT_21):
                Curse(0, 0)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrarefsp03_00', 3)
    physicsYImpulse(6000)
    setGravity(-1500)
    RandSpeedX(-1000, 1000)
    RandAddAcceleration(-250, 250)
    RandAddGravity(-250, 250)
    label(0)
    sprite('vrarefsp03_01', 3)
    sprite('vrarefsp03_00', 3)
    loopRest()
    gotoLabel(0)

@State
def ar430_Warm_Atk_OD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(2)
        Damage(160)
        MinimumDamage(10)
        AttackP2(60)
        SingleProration(1)
        PushbackX(-6000)
        Hitstop(0)
        EnemyHitstopAddition(0, 2, 2)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(-2000)
        AirPushbackY(4000)
        AirUntechableTime(60)
        HitsparkSize(400)
        ReduceHitEffects(1)
        StarterRating(2)
        DamageEffect(2, 'Bughit')
        AttackDirection(4)

        def upon_OPPONENT_HIT_OR_BLOCK():
            if (not SLOT_8):
                Curse(500, 150)
        AttackType(4)
        VoodooDamageMultiplier(2)
        BlendMode_Normal()
        ContinueState(30)

        def upon_44():
            AttackOff()

        def upon_FRAME_STEP():
            if (not SLOT_21):
                Curse(0, 0)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vrarefsp03_00', 3)
    physicsYImpulse(6000)
    setGravity(-1500)
    RandSpeedX(-1000, 1000)
    RandAddAcceleration(-250, 250)
    RandAddGravity(-250, 250)
    label(0)
    sprite('vrarefsp03_01', 3)
    sprite('vrarefsp03_00', 3)
    loopRest()
    gotoLabel(0)

@State
def ar430_Warm():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        ContinueState(30)
    sprite('vrarefsp03_00', 3)
    physicsYImpulse(6000)
    setGravity(-1500)
    RandSpeedX(-1000, 1000)
    RandSpeedX(-1000, 1000)
    RandAddAcceleration(-250, 250)
    RandAddGravity(-250, 250)
    label(0)
    sprite('vrarefsp03_01', 3)
    sprite('vrarefsp03_00', 3)
    loopRest()
    gotoLabel(0)

@State
def Marking():

    def upon_IMMEDIATE():
        SetZVal(500)

        def upon_16():
            PrivateFunction3(22, 0, 0, 100, 1)
        Eff3DEffect('efar_mark.DIG', 'efar_mark_mot_000.mmot')
        RemoveOnContact(22)
    sprite('null', 32767)
    PrivateSE('arse_23')

@State
def aref_ar431_A():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(180)
        MinimumDamage(12)
        AttackP1(80)
        AttackP2(98)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-1000)
        AirUntechableTime(120)
        Hitstop(1)
        HeatGainMultiplier(0)
        HitsparkSize(600)
        ReduceHitEffects(1)
        StarterRating(0)
        CHStateIfCHStart(3)
        VoodooDamageMultiplier(3)
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vraref431_00', 3)

@State
def aref_ar431_AOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(4)
        Damage(180)
        MinimumDamage(12)
        AttackP1(80)
        AttackP2(98)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-1000)
        AirUntechableTime(120)
        Hitstop(1)
        HeatGainMultiplier(0)
        HitsparkSize(600)
        ReduceHitEffects(1)
        StarterRating(0)
        AttackType(4)
        CHStateIfCHStart(3)
        VoodooDamageMultiplier(3)
        CancelIfPlayerHit(3)
        RemoveOnCallStateEnd(3)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vraref431_00', 3)

@State
def aref431_attack():

    def upon_IMMEDIATE():
        LinkParticle('aref_ar431_attackparts')
    sprite('null', 60)
    CreateParticle('aref_ar431_attack', -1)

@State
def aref431_Parts():

    def upon_IMMEDIATE():
        LinkParticle('aref_ar431_attackparts')
    sprite('null', 60)
    Size(1500)

@State
def aref431_attackOD():

    def upon_IMMEDIATE():
        LinkParticle('aref_ar431_attack')
    sprite('null', 60)
    SetScaleX(2500)
    SetScaleY(2000)
    CreateObject('aref431_Parts', -1)

@State
def WarmLand():

    def upon_IMMEDIATE():
        LinkParticle('aref_spLandhit')
    sprite('null', 300)

@State
def SPAClash():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        ParticleColorFromPalette(6, 6, 6)
        CallCustomizableParticle('aref_spAclash', -1)
    sprite('null', 300)

@State
def SPCLandMark():

    def upon_IMMEDIATE():
        LinkParticle('aref_spCLandMark')
    sprite('null', 300)

@State
def SPDLandBirth():

    def upon_IMMEDIATE():
        PaletteIndex(2)
        ParticleColorFromPalette(88, 0, 0)
        CallPrivateEffect('aref_spDLand')
        AddX(-16000)
    sprite('null', 300)

@Subroutine
def DriveInsectInit():
    AttackLevel_(3)
    BonusProration(110)
    DamageEffect(2, 'Bughit')
    StarterRating(2)
    AutoHitSignalSending(0)
    AttackDirection(3)
    sendToLabelUpon(2, 1)
    BlendMode_Normal()
    PaletteIndex(2)
    if SLOT_95:
        PaletteIndex(3)
    SetZVal(-500)
    TurnParticleColorable1(1)
    Unknown3054(179, 130)
    Unknown3054(178, 110)
    Unknown3054(177, 90)
    Unknown3054(176, 70)
    SLOT_9 = (SLOT_9 + 1)

    def upon_STATE_END():
        SLOT_9 = (SLOT_9 + (-1))

@State
def WarmA():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        Damage(500)
        AttackP1(70)
        AttackP2(89)
        PushbackX(-15300)
        AirPushbackX(-5300)
        AirUntechableTime(24)
        Hitstop(16)
        callSubroutine('DriveInsectInit')
        ContinueState(120)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)

        def upon_54():
            EndMomentum(1)
            sendToLabel(2)
        SetPosXByScreenPer(100)
        AbsoluteY(580000)
        physicsXImpulse(-13000)
        physicsYImpulse(8000)
        setGravity(1000)

        def upon_36():
            physicsXImpulse(-23000)
            setGravity(800)

        def upon_38():
            physicsXImpulse(-6000)
            setGravity(1400)
    sprite('vraref_spA_00', 32767)
    label(1)
    sprite('vraref_spA_01', 3)
    CommonSE('012_stab_fast')
    setGravity(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    LandingEffects(100, 1, 1)
    sprite('vraref_spA_02', 3)
    sprite('vraref_spA_03', 4)
    setGravity(1000)
    physicsXImpulse(-4000)
    physicsYImpulse(22000)
    sprite('vraref_spA_04', 80)
    clearUponHandler(2)
    sendToLabelUpon(2, 2)
    label(2)
    sprite('null', 1)
    CreateObject('SPAClash', -1)
    clearUponHandler(2)
    clearUponHandler(54)
    AttackOff()
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(200)
    sprite('vraref_spA_05', 4)
    sprite('vraref_spA_06', 4)
    loopRest()

@State
def WarmB():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        Damage(450)
        AttackP1(80)
        AttackP2(79)
        SingleProration(1)
        AirHitstunAnimation(13)
        AirPushbackX(10000)
        AirPushbackY(30000)
        AirUntechableTime(36)
        Hitstop(6)
        callSubroutine('DriveInsectInit')
        ContinueState(80)
        clearUponHandler(2)

        def upon_ON_HIT_OR_BLOCK():
            AddActionMark(1)
            XImpulseAcceleration(80)
            YAccel(80)
            if (SLOT_2 == 3):
                NoAttackDuringAction(1)
                sendToLabel(1)
        sendToLabelUpon(44, 1)
        AbsoluteY(0)
        SetPosXByScreenPer(40)

        def upon_36():
            SetPosXByScreenPer(10)

        def upon_38():
            SetPosXByScreenPer(70)
    sprite('vraref_spB_00ex00', 1)
    sprite('vraref_spB_00ex00', 3)
    CreateObject('SPCLandMark', 0)
    CommonSE('012_stab_fast')
    sprite('vraref_spB_01ex00', 4)
    sprite('vraref_spB_02ex00', 4)
    CreateObject('WarmLand', 0)
    sprite('vraref_spB_03ex00', 3)
    SetAcceleration(1400)
    setGravity(-1120)
    RefreshMultihit()
    sprite('vraref_spB_04ex00', 3)
    SLOT_51 = 30
    RefreshMultihit()
    label(0)
    sprite('vraref_spB_03ex00', 3)
    SLOT_51 = (SLOT_51 + (-1))
    RefreshMultihit()
    sprite('vraref_spB_04ex00', 3)
    RefreshMultihit()
    loopRest()
    if SLOT_51:
        _gotolabel(0)
    label(1)
    sprite('vraref_spB_03ex00', 3)
    EndMomentum(1)
    AlphaValue(200)
    ConstantAlphaModifier(-10)
    clearUponHandler(10)
    clearUponHandler(44)
    AttackOff()
    sprite('vraref_spB_04ex00', 3)
    sprite('vraref_spB_03ex00', 3)
    sprite('vraref_spB_04ex00', 3)
    sprite('vraref_spB_03ex00', 3)
    sprite('vraref_spB_04ex00', 3)

@State
def WarmC():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        Damage(940)
        AttackP1(70)
        AttackP2(89)
        MoveAttributes(0, 0, 0, 1, 0)
        Hitstop(25)
        GroundedHitstunAnimation(2)
        PushbackX(-45750)
        AirPushbackX(-5300)
        GuardCrush(100, 1)
        GuardCrushHitstun(35)
        SetActionMark(481)
        callSubroutine('DriveInsectInit')
        ContinueState(100)
        sendToLabelUpon(44, 2)
        SetPosXByScreenPer(65)
        AbsoluteY(0)
        Size(750)
        SetScaleSpeed(4)

        def upon_36():
            SetPosXByScreenPer(35)

        def upon_38():
            SetPosXByScreenPer(95)
    sprite('vraref_spC_09', 1)
    sprite('vraref_spC_08', 1)
    CreateObject('SPCLandMark', -1)
    sprite('vraref_spC_00', 2)
    sprite('vraref_spC_01', 15)
    sprite('vraref_spC_01', 30)
    CharacterFlash(-6579356, 5, 6)
    sprite('vraref_spC_00', 2)
    SetScaleSpeed(0)
    Size(750)
    sprite('vraref_spC_08', 1)
    sprite('vraref_spC_02', 2)
    Size(1000)
    sprite('vraref_spC_03', 11)
    CreateObject('WarmLand', -1)
    physicsXImpulse(-13500)
    physicsYImpulse(28000)
    setGravity(2500)
    label(0)
    sprite('vraref_spC_04', 3)
    AddRotationPerFrame(-3000)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(2)
    clearUponHandler(44)
    AddX(-100000)
    AddRotationPerFrame(0)
    RotationAngle(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    sprite('vraref_spC_05', 3)
    CreateObject('WarmLand', -1)
    SetScaleSpeed(-5)
    sprite('vraref_spC_07', 3)
    ConstantAlphaModifier(-20)
    sprite('vraref_spC_08', 2)
    sprite('vraref_spC_09', 2)
    ExitState()
    label(2)
    clearUponHandler(2)
    clearUponHandler(10)
    clearUponHandler(44)
    EndAttack()
    AddRotationPerFrame(0)
    RotationAngle(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    CreateObject('WarmLand', -1)
    SetScaleSpeed(-5)
    ConstantAlphaModifier(-20)
    sprite('vraref_spC_08', 2)
    sprite('vraref_spC_09', 2)

@State
def WarmD():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        Damage(250)
        AttackP1(80)
        AttackP2(79)
        SingleProration(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(0)
        AirUntechableTime(40)
        HardKnockdown(1)
        Hitstop(1)
        EnemyHitstopAddition(0, -1, -1)
        HitsparkSize(300)
        ReduceHitEffects(1)
        callSubroutine('DriveInsectInit')
        ContinueState(200)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 0)

        def upon_54():
            EndMomentum(1)
            sendToLabel(3)
        AbsoluteY(3000000)
        SetPosXByScreenPer(35)
        physicsXImpulse(4500)
        physicsYImpulse(-55000)
        setGravity(-500)

        def upon_36():
            SetPosXByScreenPer(5)

        def upon_38():
            SetPosXByScreenPer(65)

        def upon_FRAME_STEP():
            PrivateFunction4(-20)
            if (SLOT_23 >= SLOT_0):
                if SLOT_51:
                    DeleteObject(23)
    sprite('vraref_spD_00', 3)
    label(0)
    sprite('vraref_spD_01', 3)
    RefreshMultihit()
    sprite('vraref_spD_02', 3)
    RefreshMultihit()
    sprite('vraref_spD_03', 3)
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    Damage(940)
    AirUntechableTime(50)
    AirPushbackX(1000)
    AirPushbackY(48000)
    Hitstop(14)
    AddY(32000)
    sprite('null', 15)
    CreateObject('WarmLand', -1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    SLOT_51 = 1
    sprite('vraref_spD_03ex00', 1)
    CreateObject('SPDLandBirth', -1)
    sprite('vraref_spD_03ex01', 1)
    sprite('vraref_spD_03ex02', 1)
    RefreshMultihit()
    physicsXImpulse(2000)
    physicsYImpulse(30000)
    label(2)
    sprite('vraref_spD_04', 3)
    sprite('vraref_spD_05', 3)
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('keep', 10)
    clearUponHandler(2)
    clearUponHandler(3)
    clearUponHandler(54)
    EndAttack()
    AddRotationPerFrame(0)
    RotationAngle(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    SetScaleSpeed(-5)
    ConstantAlphaModifier(-20)

@State
def Warm_Ultimate():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        Damage(500)
        AttackP1(70)
        HeatGainMultiplier(0)
        MinimumDamage(0)
        ChipPercentage(0)
        Hitstop(3)
        AirUntechableTime(100)
        AirHitstunAnimation(17)
        AirPushbackX(6500)
        AirPushbackY(30000)
        PushbackX(8000)
        StarterRating(2)
        DamageEffect(2, 'Bughit')
        AutoHitSignalSending(0)
        SameMoveProration(-1)

        def upon_FRAME_STEP():
            if SLOT_30:
                SLOT_52 = 1
            else:
                SLOT_52 = 0
            if SLOT_53:
                if (not SLOT_52):
                    SLOT_53 = (SLOT_53 + 1)
                if (SLOT_53 >= 31):
                    if SLOT_51:
                        Flip()
                        EndMomentum(1)
                        AbsoluteY(350000)
                        physicsXImpulse(18000)
                        SetAcceleration(200)
                        physicsYImpulse(-2000)
                        SetPosXByScreenPer(-25)
                        RefreshMultihit()
                        SLOT_53 = 0
                        SLOT_54 = 0
                        SLOT_55 = 0
                        sendToLabel(1)
                    else:
                        sendToLabel(9)
            elif SLOT_38:
                PrivateFunction5(120)
                if (SLOT_22 < SLOT_0):
                    SLOT_53 = 1
            else:
                PrivateFunction5(120)
                if (SLOT_22 > SLOT_0):
                    SLOT_53 = 1
            SLOT_54 = (SLOT_54 + (-1))
            if (not SLOT_IsInOverdrive2):
                if (not (SLOT_55 >= 8)):
                    RefreshMultihit()
            if (not SLOT_4):
                SLOT_51 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_54 = 6
            SLOT_55 = (SLOT_55 + 1)
            XImpulseAcceleration(95)
        SLOT_51 = 1

        def upon_STATE_END():
            SLOT_7 = (SLOT_7 + (-1))
        BlendMode_Normal()
        PaletteIndex(2)
        if SLOT_95:
            PaletteIndex(3)
        SetZVal(-500)
        TurnParticleColorable1(1)
        Unknown3054(179, 130)
        Unknown3054(178, 110)
        Unknown3054(177, 90)
        Unknown3054(176, 70)
    sprite('null', 30)
    PrivateSE('arse_03')
    loopRest()
    AbsoluteY(350000)
    physicsXImpulse(18000)
    SetAcceleration(200)
    physicsYImpulse(-2000)
    SetPosXByScreenPer(-25)
    label(1)
    sprite('vraref441_00', 10)
    sprite('vraref441_01', 8)
    sprite('vraref441_02', 8)
    sprite('vraref441_03', 8)
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 1)
    EndAttack()

@State
def Warm_UltimateOD():

    def upon_IMMEDIATE():
        AttackDefaults_SuperProjectile()
        AttackLevel_(5)
        Damage(500)
        AttackP1(70)
        HeatGainMultiplier(0)
        MinimumDamage(0)
        ChipPercentage(0)
        Hitstop(3)
        AirUntechableTime(100)
        AirHitstunAnimation(17)
        AirPushbackX(6500)
        AirPushbackY(30000)
        PushbackX(8000)
        StarterRating(2)
        DamageEffect(2, 'Bughit')
        AutoHitSignalSending(0)
        AttackType(4)
        SameMoveProration(-1)

        def upon_FRAME_STEP():
            if SLOT_30:
                SLOT_52 = 1
            else:
                SLOT_52 = 0
            if SLOT_53:
                if (not SLOT_52):
                    SLOT_53 = (SLOT_53 + 1)
                if (SLOT_53 >= 11):
                    if SLOT_51:
                        Flip()
                        EndMomentum(1)
                        AbsoluteY(350000)
                        physicsXImpulse(18000)
                        SetAcceleration(200)
                        physicsYImpulse(-2000)
                        SetPosXByScreenPer(-25)
                        RefreshMultihit()
                        SLOT_53 = 0
                        SLOT_54 = 0
                        SLOT_55 = 0
                        sendToLabel(1)
                    else:
                        sendToLabel(9)
            elif SLOT_38:
                PrivateFunction5(120)
                if (SLOT_22 < SLOT_0):
                    SLOT_53 = 1
            else:
                PrivateFunction5(120)
                if (SLOT_22 > SLOT_0):
                    SLOT_53 = 1
            SLOT_54 = (SLOT_54 + (-1))
            if (not SLOT_IsInOverdrive2):
                RefreshMultihit()
            if (not SLOT_4):
                SLOT_51 = 0

        def upon_OPPONENT_HIT_OR_BLOCK():
            SLOT_54 = 6
            XImpulseAcceleration(95)
        SLOT_51 = 1

        def upon_STATE_END():
            SLOT_7 = (SLOT_7 + (-1))
        BlendMode_Normal()
        PaletteIndex(2)
        if SLOT_95:
            PaletteIndex(3)
        SetZVal(-500)
        TurnParticleColorable1(1)
        Unknown3054(179, 130)
        Unknown3054(178, 110)
        Unknown3054(177, 90)
        Unknown3054(176, 70)
    sprite('null', 30)
    PrivateSE('arse_03')
    loopRest()
    AbsoluteY(350000)
    physicsXImpulse(18000)
    SetAcceleration(200)
    physicsYImpulse(-2000)
    SetPosXByScreenPer(-25)
    label(1)
    sprite('vraref441_00', 10)
    sprite('vraref441_01', 8)
    sprite('vraref441_02', 8)
    sprite('vraref441_03', 8)
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 1)
    EndAttack()

@State
def RLAstFire():

    def upon_IMMEDIATE():
        LinkParticle('aref_RlAstfire')
        RemoveOnCallStateEnd(3)
        IgnoreScreenfreeze(1)
        SetZVal(-100)
    sprite('null', 120)
    AlphaValue(0)
    ConstantAlphaModifier(2)
    sprite('null', 32767)
    ConstantAlphaModifier(0)

@State
def CurseShotTest():

    def upon_IMMEDIATE():
        AttackDefaults_Projectile()
        BlendMode_Normal()
        AttackLevel_(3)
        ProjectileLevel(0)
        Damage(0)
        HeatGainMultiplier(0)
        Hitstop(0)
        AttackDirection(1)
        ContinueState(900)
        FaceLeft()
        EndAttack()
        AddY(250000)
        sendToLabelUpon(10, 2)
        sendToLabelUpon(32, 10)
        HitsPerCall(1, 0, 0, 0, 0, 0, 1, 1)
        sendToLabelUpon(54, 10)

        def upon_FRAME_STEP():
            if (SLOT_98 < 150000):
                Unknown23144(22, 0, 103, 0, 0, 0, 0, 0, 90, 0, 3)
                clearUponHandler(3)
                SLOT_32 = 480
                PrivateSE('arse_23')
                Size(1500)
                sendToLabel(2)
        sendToLabelUpon(53, 10)
    sprite('null', 9)
    PaletteIndex(2)
    if SLOT_95:
        PaletteIndex(3)
    ParticleColorFromPalette(192, 193, 194)
    CallPrivateEffect('aref_ar400_A')
    Visibility(1)
    loopRest()
    label(1)
    sprite('vraref400_01', 1)
    CopyFromRightToLeft(23, 2, 51, 22, 2, 22)
    PrivateFunction(1, 2, 22, 2, 51, 2, 51)
    PrivateFunction(3, 2, 51, 0, 60, 2, 12)
    CopyFromRightToLeft(23, 2, 52, 22, 2, 23)
    PrivateFunction(1, 2, 23, 2, 52, 2, 52)
    PrivateFunction(0, 2, 52, 0, -200000, 2, 52)
    PrivateFunction(3, 2, 52, 0, -50, 2, 13)
    loopRest()
    GotoIf0(10, 2, 21)
    gotoLabel(1)
    label(2)
    sprite('vraref400_01', 32767)
    SetActionMark(1)

    def upon_16():
        PrivateFunction3(22, 0, 0, 60, 1)
    sprite('vraref400_01', 32767)
    label(10)
    clearUponHandler(10)
    clearUponHandler(54)
    clearUponHandler(32)
    clearUponHandler(3)
    clearUponHandler(45)
    sprite('null', 30)
    SLOT_32 = 0
    BlendMode_Normal()
    ConstantAlphaModifier(-20)
    SetScaleSpeed(100)
    CreateObject('aref_hit_insect', -1)

@State
def SpecialShotTest():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        AttackP1(80)
        Damage(940)
        AirUntechableTime(30)
        GroundedHitstunAnimation(9)
        AirPushbackX(2000)
        AirPushbackY(10000)
        MoveAttributes(0, 0, 0, 1, 0)
        DamageEffect(2, 'Bughit')
        AutoHitSignalSending(0)
        Unknown12052(1)

        def upon_OPPONENT_HIT_OR_BLOCK():
            if (not SLOT_8):
                if (not SLOT_110):
                    Curse(2000, 1000)
                if SLOT_110:
                    Curse(3000, 2000)
        BlendMode_Normal()
        PaletteIndex(2)
        if SLOT_95:
            PaletteIndex(3)
        ContinueState(400)
        SetZVal(-500)
        TurnParticleColorable1(1)
        Unknown3054(179, 130)
        Unknown3054(178, 110)
        Unknown3054(177, 90)
        Unknown3054(176, 70)
        HitsPerCall(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 1)
        sendToLabelUpon(2, 1)

        def upon_33():
            SetPosXByScreenPer(15)

        def upon_34():
            SetPosXByScreenPer(55)

        def upon_35():
            SetPosXByScreenPer(95)
        SetPosYByScreenPer(1)
        AttackOff()
        if SLOT_137:
            DamageMultiplier(80)
    sprite('vraref404_00', 6)
    physicsYImpulse(-5000)
    sprite('vraref404_00', 6)
    CommonSE('022_magiccircle_c')
    sprite('vraref404_01', 6)
    physicsYImpulse(0)
    sprite('vraref404_00', 6)
    sprite('vraref404_01', 6)
    RefreshMultihit()
    physicsYImpulse(-30000)
    setGravity(2500)
    label(0)
    sprite('vraref404_00', 6)
    sprite('vraref404_01', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(2)
    clearUponHandler(54)
    sprite('keep', 3)
    EndMomentum(1)
    CommonSE('012_stab_fast')
    sprite('vraref404_00', 6)
    setGravity(-1000)
    sprite('vraref404_01', 6)
    AttackOff()
    sprite('vraref404_00', 6)
    sprite('vraref404_01', 6)
    sprite('vraref404_00', 6)
    sprite('vraref404_01', 6)
    sprite('vraref404_00', 6)
    AlphaValue(200)
    ConstantAlphaModifier(-6)
    sprite('vraref404_01', 6)
    sprite('vraref404_00', 6)
    sprite('vraref404_01', 6)
    sprite('vraref404_00', 6)
    sprite('vraref404_01', 6)
    sprite('vraref404_00', 6)
    sprite('vraref404_01', 6)
    sprite('vraref404_00', 6)

@State
def ar407_Dummy():

    def upon_IMMEDIATE():
        AttackDefaults_SpecialProjectile()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        SingleProration(1)
        AirUntechableTime(200)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirPushbackX(0)
        AirPushbackY(1)
        YImpulseBeforeWallbounce(-200)
        OnlyHitPlayer(1)
        PassByArmor(1)
        StarterRating(2)
        Unknown12052(1)
        FatalCounter(1)
        EnableCollision(1)
        SetYCollisionFromOrigin(1)
        ArakuneSpriteOverlay('vraref000_00', 160, 0, 0, 500, 0, 2147483647, 1000, 1000)
        AlphaIsColorOnPalette(179, 130)
        AlphaIsColorOnPalette(178, 110)
        AlphaIsColorOnPalette(177, 90)
        AlphaIsColorOnPalette(176, 70)
        BlendMode_Normal()
        ForceShadowOn(1)

        def upon_OPPONENT_HIT():
            clearUponHandler(12)

            def upon_41():
                sendToLabel(6)
            sendToLabel(1)

        def upon_32():
            CopyFromRightToLeft(23, 2, 12, 2, 2, 12)
            CopyFromRightToLeft(23, 2, 13, 2, 2, 13)
            XImpulseAcceleration(30)
            setGravity(1150)

        def upon_33():
            physicsYImpulse(8000)
            physicsXImpulse(7000)
            setGravity(1200)

        def upon_34():
            ForceFaceSprite()
            physicsYImpulse(12000)
            physicsXImpulse(7000)
            setGravity(1200)

        def upon_35():
            physicsYImpulse(18000)
            physicsXImpulse(8000)
            setGravity(1200)

        def upon_36():
            ForceFaceSprite()
            physicsYImpulse(8000)
            physicsXImpulse(4000)
            setGravity(1200)
        if SLOT_137:
            DamageMultiplier(80)
    sprite('ar407_00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_01', 4)
    sprite('ar407_02', 4)
    sprite('ar407_03', 6)
    sprite('ar407_09', 3)
    sprite('ar407_09ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_09ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_09ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_09ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_09ex02', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_09ex02', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_09ex03', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_09ex03', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_09ex04', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_09ex04', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    ExitState()
    label(1)
    sprite('ar407_04', 5)
    EndMomentum(1)

    def upon_FRAME_STEP():
        PrivateFunction3(22, 0, 250000, 15, 0)
        if (not Unknown23146(22, 'ar407_Dummy')):
            NoAttackDuringAction(1)
            sendToLabel(6)
        CopyFromRightToLeft(23, 2, 51, 22, 2, 23)
        if (SLOT_54 >= 1800000):
            ApplyFunctionsToObjects(22)
            AbsoluteY(1800000)
            ApplyFunctionsToSelf()
        if SLOT_2:
            SLOT_2 = (SLOT_2 + 1)
            if (SLOT_2 > 11):
                SetActionMark(1)
    RenderLayer(6)
    sprite('ar407_05', 5)
    CreateObject('aref_407_WebBall', -1)
    SLOT_52 = (SLOT_52 + 1)
    sprite('ar407_06', 5)
    SLOT_52 = (SLOT_52 + 1)
    if SLOT_6:
        _gotolabel(6)
    sprite('ar407_07', 5)
    E0EAEffectPosition(22)
    PrivateFunction3(0, 0, 0, 0, 0)
    SetActionMark(1)
    physicsXImpulse(2500)
    sprite('ar407_08', 5)
    SLOT_6 = 1
    sprite('ar407_06', 5)
    sprite('ar407_07', 5)
    sprite('ar407_08', 5)
    sprite('ar407_06', 5)
    sprite('ar407_07', 5)
    sprite('ar407_08', 5)
    sprite('ar407_06', 5)
    sprite('ar407_07', 5)
    sprite('ar407_08', 5)
    sprite('ar407_06', 5)
    sprite('ar407_07', 5)
    sprite('ar407_08', 5)
    sprite('ar407_06', 5)
    sprite('ar407_07', 5)
    sprite('ar407_08', 5)
    sprite('ar407_06', 5)
    sprite('ar407_07', 5)
    sprite('ar407_08', 5)
    loopRest()
    clearUponHandler(3)
    E0EAEffectPosition(0)
    gotoLabel(7)
    label(6)
    sprite('keep', 1)
    clearUponHandler(41)
    clearUponHandler(3)
    E0EAEffectPosition(0)
    PrivateFunction3(0, 0, 0, 0, 0)
    PassbackAddActionMarkToFunction('aref_407_WebBall', 32)
    if (SLOT_52 == 1):
        sendToLabel(8)
    elif (SLOT_52 == 0):
        sendToLabel(9)
    label(7)
    sprite('ar407_06ex00', 1)
    PassbackAddActionMarkToFunction('aref_407_WebBall', 32)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    AttackLevel_(1)
    Damage(0)
    Hitstop(0)
    AirUntechableTime(10)
    AirHitstunAnimationReset()
    ResetPushback()
    AirPushbackY(16000)
    ResetGravity()
    PassByArmor(1)
    CounterHitSetting(1)
    DefeatOpponentBehavior(1)
    DamageEffect(5, '')
    ShutUp(1)
    EnableRapidCancel(0)
    RefreshMultihit()
    physicsYImpulse(4000)
    sprite('ar407_06ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_06ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_06ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_07ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_07ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_07ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_07ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_08ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_08ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_08ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_08ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_06ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_06ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_06ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_06ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_07ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_07ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_07ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_07ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    ExitState()
    label(8)
    sprite('ar407_05ex00', 1)
    PassbackAddActionMarkToFunction('aref_407_WebBall', 32)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    AttackLevel_(1)
    Damage(0)
    Hitstop(0)
    AirUntechableTime(10)
    AirHitstunAnimationReset()
    ResetPushback()
    AirPushbackY(16000)
    ResetGravity()
    DamageEffect(5, '')
    RefreshMultihit()
    sprite('ar407_05ex00', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_05ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_05ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_05ex02', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_05ex02', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_05ex03', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_05ex03', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_05ex04', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_05ex04', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    ExitState()
    label(9)
    sprite('ar407_04ex00', 1)
    PassbackAddActionMarkToFunction('aref_407_WebBall', 32)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    AttackLevel_(1)
    Damage(0)
    Hitstop(0)
    AirUntechableTime(10)
    AirHitstunAnimationReset()
    ResetPushback()
    AirPushbackY(16000)
    ResetGravity()
    DamageEffect(5, '')
    RefreshMultihit()
    sprite('ar407_04ex00', 1)
    sprite('ar407_04ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_04ex01', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_04ex02', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_04ex02', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_04ex03', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_04ex03', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_04ex04', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    sprite('ar407_04ex04', 1)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)
    CreateObject('aref_ar402_A', 106)

@State
def MukadeMatome():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        Size(1200)
    sprite('null', 10)
    CreateObject('MukadeEye', -1)
    ApplyFunctionsToObjects(1)
    AddY(-150000)
    AddX(300000)
    ApplyFunctionsToSelf()
    sprite('null', 10)
    CreateObject('MukadeEye2', -1)
    ApplyFunctionsToObjects(1)
    AddY(200000)
    AddX(-500000)
    ApplyFunctionsToSelf()
    sprite('null', 10)
    CreateObject('MukadeEye', -1)
    ApplyFunctionsToObjects(1)
    AddY(500000)
    AddX(400000)
    ApplyFunctionsToSelf()
    sprite('null', 10)
    CreateObject('MukadeEye', -1)
    ApplyFunctionsToObjects(1)
    AddY(700000)
    AddX(-250000)
    ApplyFunctionsToSelf()
    sprite('null', 10)
    CreateObject('MukadeEye', -1)
    ApplyFunctionsToObjects(1)
    AddY(150000)
    AddX(950000)
    ApplyFunctionsToSelf()
    sprite('null', 10)
    CreateObject('MukadeHead00', -1)
    ApplyFunctionsToObjects(1)
    AddY(-150000)
    AddX(300000)
    ApplyFunctionsToSelf()
    CreateObject('MukadeBodyIppai00', -1)
    ApplyFunctionsToObjects(1)
    AddY(-150000)
    AddX(300000)
    ApplyFunctionsToSelf()
    sprite('null', 10)
    CreateObject('MukadeHead00', -1)
    ApplyFunctionsToObjects(1)
    AddY(200000)
    AddX(-600000)
    RotationAngle(450000)
    ApplyFunctionsToSelf()
    CreateObject('MukadeBodyIppai00', -1)
    ApplyFunctionsToObjects(1)
    AddY(200000)
    AddX(-600000)
    RotationAngle(450000)
    ApplyFunctionsToSelf()
    sprite('null', 10)
    CreateObject('MukadeHead00', -1)
    ApplyFunctionsToObjects(1)
    AddY(500000)
    AddX(400000)
    RotationAngle(0)
    ApplyFunctionsToSelf()
    CreateObject('MukadeBodyIppai00', -1)
    ApplyFunctionsToObjects(1)
    AddY(500000)
    AddX(400000)
    RotationAngle(0)
    ApplyFunctionsToSelf()
    sprite('null', 10)
    CreateObject('MukadeHead00', -1)
    ApplyFunctionsToObjects(1)
    AddY(750000)
    AddX(-300000)
    RotationAngle(180000)
    ApplyFunctionsToSelf()
    CreateObject('MukadeBodyIppai00', -1)
    ApplyFunctionsToObjects(1)
    AddY(750000)
    AddX(-300000)
    RotationAngle(180000)
    ApplyFunctionsToSelf()
    sprite('null', 10)
    CreateObject('MukadeBodyIppai01', -1)
    ApplyFunctionsToObjects(1)
    AddY(900000)
    RotationAngle(180000)
    Flip()
    ApplyFunctionsToSelf()
    CreateObject('MukadeHead01', -1)
    ApplyFunctionsToObjects(1)
    AddY(900000)
    RotationAngle(180000)
    Flip()
    ApplyFunctionsToSelf()
    sprite('null', 10)
    CreateObject('MukadeBodyIppai02', -1)
    ApplyFunctionsToObjects(1)
    AddY(150000)
    AddX(950000)
    RotationAngle(250000)
    ApplyFunctionsToSelf()
    CreateObject('MukadeHead02', -1)
    ApplyFunctionsToObjects(1)
    AddY(150000)
    AddX(950000)
    RotationAngle(250000)
    ApplyFunctionsToSelf()

@State
def MukadeHead00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('aref_mukade00', '')
        IgnoreScreenfreeze(1)
        E0EAEffectRotation(2)
        Size(1200)
    sprite('null', 30)
    sprite('null', 150)

@State
def MukadeBodyIppai00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        E0EAEffectRotation(2)
    sprite('null', 27)
    sprite('null', 27)
    CreateObject('MukadeBody00', -1)
    sprite('null', 27)
    CreateObject('MukadeBody00', -1)
    sprite('null', 27)
    CreateObject('MukadeBody00', -1)
    sprite('null', 27)
    CreateObject('MukadeBody00', -1)
    sprite('null', 27)
    CreateObject('MukadeBody00', -1)
    sprite('null', 27)
    CreateObject('MukadeBody00', -1)
    sprite('null', 100)
    CreateObject('MukadeTail00', -1)

@State
def MukadeBody00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('aref_mukade01', '')
        IgnoreScreenfreeze(1)
        Size(1300)
        E0EAEffectRotation(2)
    sprite('null', 50)
    sprite('null', 150)

@State
def MukadeTail00():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('aref_mukade02', '')
        IgnoreScreenfreeze(1)
        Size(1300)
        E0EAEffectRotation(2)
    sprite('null', 50)
    sprite('null', 150)

@State
def MukadeHead01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('aref_mukade00', '')
        IgnoreScreenfreeze(1)
        Size(1500)
        E0EAEffectRotation(2)
        SetZVal(-500)
    sprite('null', 30)
    sprite('null', 150)

@State
def MukadeBodyIppai01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        E0EAEffectRotation(2)
    sprite('null', 27)
    sprite('null', 27)
    CreateObject('MukadeBody01', -1)
    sprite('null', 27)
    CreateObject('MukadeBody01', -1)
    sprite('null', 27)
    CreateObject('MukadeBody01', -1)
    sprite('null', 27)
    CreateObject('MukadeBody01', -1)
    sprite('null', 27)
    CreateObject('MukadeBody01', -1)
    sprite('null', 100)
    CreateObject('MukadeTail01', -1)

@State
def MukadeBody01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('aref_mukade01', '')
        IgnoreScreenfreeze(1)
        Size(1500)
        E0EAEffectRotation(2)
        SetZVal(-500)
    sprite('null', 50)
    sprite('null', 150)

@State
def MukadeTail01():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('aref_mukade02', '')
        IgnoreScreenfreeze(1)
        Size(1500)
        E0EAEffectRotation(2)
        SetZVal(-500)
    sprite('null', 50)
    sprite('null', 200)

@State
def MukadeHead02():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('aref_temaemukade00', '')
        IgnoreScreenfreeze(1)
        Size(1500)
        E0EAEffectRotation(2)
        SetZVal(-1000)
    sprite('null', 60)
    AlphaValue(0)
    sprite('null', 100)
    AlphaValue(255)
    sprite('null', 200)

@State
def MukadeBodyIppai02():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        IgnoreScreenfreeze(1)
        E0EAEffectRotation(2)
    sprite('null', 24)
    sprite('null', 24)
    CreateObject('MukadeBody02', -1)
    sprite('null', 24)
    CreateObject('MukadeBody02', -1)
    sprite('null', 24)
    CreateObject('MukadeBody02', -1)
    sprite('null', 24)
    CreateObject('MukadeBody02', -1)
    sprite('null', 35)
    CreateObject('MukadeBody02', -1)
    sprite('null', 100)
    CreateObject('MukadeTail02', -1)

@State
def MukadeBody02():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('aref_temaemukade01', '')
        IgnoreScreenfreeze(1)
        Size(1500)
        E0EAEffectRotation(2)
        SetZVal(-1000)
    sprite('null', 60)
    AlphaValue(0)
    sprite('null', 100)
    AlphaValue(255)
    sprite('null', 300)

@State
def MukadeTail02():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('aref_temaemukade02', '')
        IgnoreScreenfreeze(1)
        Size(1500)
        E0EAEffectRotation(2)
        SetZVal(-1000)
    sprite('null', 60)
    AlphaValue(0)
    sprite('null', 100)
    AlphaValue(255)
    sprite('null', 300)

@State
def MukadeEye():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('aref_medama', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        Size(1200)
        SetZVal(1000)
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    sprite('null', 15)
    LinkParticle('aref_AHeyemoya_pos')
    ScreenShake(10000, 10000)
    PrivateSE('arse_06')
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def MukadeEye2():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        Eff3DEffect('aref_medama', '')
        FaceSpawnLocation()
        IgnoreScreenfreeze(1)
        Size(1200)
        SetZVal(1000)
        sendToLabelUpon(32, 0)
    sprite('null', 10)
    sprite('null', 15)
    CreateObject('MukadeEye3', -1)
    ScreenShake(10000, 10000)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    ConstantAlphaModifier(-26)

@State
def MukadeEye3():

    def upon_IMMEDIATE():
        BlendMode_Normal()
        LinkParticle('aref_AHeyemoya_pos')
        RemoveOnCallStateEnd(2)
        AddX(35000)
        IgnoreScreenfreeze(1)
        Size(1200)
    sprite('null', 32767)

    @State
    def Bloodrain():

        def upon_IMMEDIATE():
            IgnoreScreenfreeze(1)
            AddY(300000)
        sprite('null', 1)
        sprite('null', 32767)
        LinkParticle('aref_AHbloodrain_02')

    @State
    def AHnenkin():

        def upon_IMMEDIATE():
            BlendMode_Normal()
            Eff3DEffect('aref_nenkin', '')
            TeleportToObject(22)
            Size(1000)
            AlphaValue(0)
            sendToLabelUpon(32, 0)
        sprite('null', 20)
        ConstantAlphaModifier(17)
        sprite('null', 32767)
        label(0)
        sprite('null', 10)
        ConstantAlphaModifier(-26)

    @State
    def AstBlackOut():

        def upon_IMMEDIATE():
            IgnoreScreenfreeze(1)
            RenderLayer(4)
            ScreenPosition(1)
            E0EAEffectPosition(3)
            SetPosXByScreenPer(50)
            ColorForTransition(4278190080)
            Size(200000)
            BlendMode_Normal()
            AlphaValue(255)
        sprite('vraref407_03', 71)
        sprite('keep', 25)
        ConstantAlphaModifier(-10)

    @State
    def BrustDDyodare():

        def upon_IMMEDIATE():
            IgnoreScreenfreeze(1)
            IgnoreFinishStop(1)
            BlendMode_Normal()
            Eff3DEffect('aref_430yodare00', '')
        sprite('null', 5)
        CreateParticle('aref_440yodare_00', -1)
        Size(1350)
        physicsYImpulse(35000)
        sprite('null', 7)
        Size(2250)
        physicsYImpulse(0)
        sprite('null', 9)
        Eff3DEffect('aref_430yodare01', '')
        IgnoreScreenfreeze(0)
        IgnoreFinishStop(0)
        sprite('null', 4)
        SetScaleSpeed(80)
        physicsYImpulse(-28000)

    @State
    def BrustDDyodareSub():

        def upon_IMMEDIATE():
            BlendMode_Normal()
            Eff3DEffect('aref_430yodare02', '')
            AddY(75000)
            SetScaleX(1250)
        sprite('null', 20)
        sprite('null', 10)
        ConstantAlphaModifier(-26)

    @State
    def BrustDDyodareEX():

        def upon_IMMEDIATE():
            IgnoreScreenfreeze(1)
            IgnoreFinishStop(1)
            BlendMode_Normal()
            Eff3DEffect('aref_430yodare00', '')
        sprite('null', 5)
        Size(1875)
        physicsYImpulse(65000)
        ParticleSize(1000)
        CallCustomizableParticle('aref_440yodare_00', -1)
        sprite('null', 7)
        Size(3000)
        physicsYImpulse(0)
        sprite('null', 9)
        Eff3DEffect('aref_430yodare01', '')
        IgnoreScreenfreeze(0)
        IgnoreFinishStop(0)
        sprite('null', 4)
        SetScaleSpeed(80)
        physicsYImpulse(-28000)

    @State
    def aref_407_WebBall():

        def upon_IMMEDIATE():
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            IgnorePauses(2)
            IgnoreScreenfreeze(1)
            BlendMode_Normal()
            PaletteIndex(4)
            ForceBloomMaskOn(1)
            AddY(-125000)
            sendToLabelUpon(32, 0)
        sprite('vraref407_00', 4)
        CommonSE('020_blood_1')
        sprite('vraref407_01', 4)
        sprite('vraref407_02', 4)
        ApplyFunctionsToObjects(22)
        Visibility(1)
        ApplyFunctionsToSelf()
        sprite('vraref407_03', 32767)
        label(0)
        sprite('vraref407_00', 5)
        ApplyFunctionsToObjects(22)
        Visibility(0)
        ApplyFunctionsToSelf()
        CreateParticle('aref_407del', -1)
        CommonSE('020_blood_1')
        sprite('vraref407_01', 5)
        SetScaleSpeed(15)
        ConstantAlphaModifier(-25)

    @State
    def aref_441():

        def upon_IMMEDIATE():
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            IgnoreScreenfreeze(1)
            PaletteIndex(0)
        sprite('null', 3)
        CreateParticle('aref_441', -1)
        CreateParticle('aref_441aura', -1)
        label(0)
        sprite('null', 3)
        CreateParticle('aref_441aura', -1)
        CreateParticle('aref_441_b', 103)
        gotoLabel(0)

    @State
    def aref_441_powder():

        def upon_IMMEDIATE():
            RemoveOnCallStateEnd(2)
            E0EAEffectPosition(2)
            IgnoreScreenfreeze(1)
            PaletteIndex(0)
        label(0)
        sprite('null', 3)
        CreateParticle('aref_441powder', -1)
        gotoLabel(0)

    @State
    def Eventyodare():

        def upon_IMMEDIATE():
            IgnoreScreenfreeze(1)
            IgnoreFinishStop(1)
            BlendMode_Normal()
            Eff3DEffect('aref_430yodare00', '')
        sprite('null', 5)
        CreateParticle('aref_440yodare_00', -1)
        Size(1350)
        physicsYImpulse(35000)
        sprite('null', 7)
        Size(2250)
        physicsYImpulse(0)
        sprite('null', 9)
        Eff3DEffect('aref_430yodare01', '')
        IgnoreScreenfreeze(0)
        IgnoreFinishStop(0)
        sprite('null', 4)
        SetScaleSpeed(80)
        physicsYImpulse(-28000)

    @State
    def Act2EventBNCreate():

        def upon_IMMEDIATE():
            LoadSpritePalette(0)
            SetZVal(-500)
            sendToLabelUpon(32, 1)
            sendToLabelUpon(33, 2)
            AddX(160000)
        label(0)
        sprite('bn010_02', 6)
        sprite('bn010_03', 6)
        sprite('bn010_04', 6)
        sprite('bn010_05', 6)
        sprite('bn010_06', 6)
        sprite('bn010_07', 6)
        sprite('bn010_08', 6)
        sprite('bn010_09', 6)
        sprite('bn010_10', 6)
        sprite('bn010_11', 6)
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('bn010_01', 6)
        sprite('bn010_00', 6)
        sprite('bn000_00', 7)
        sprite('bn000_01', 7)
        sprite('bn032_00', 3)
        physicsXImpulse(-32000)
        Flip()
        sprite('bn032_01', 3)
        sprite('bn032_02', 3)
        CommonSE('204_runjump_normal_1')
        DashEffects(100, 1, 1)
        sprite('bn032_03', 3)
        sprite('bn032_04', 3)
        sprite('bn032_05', 3)
        sprite('bn032_06', 3)
        CommonSE('204_runjump_normal_1')
        DashEffects(100, 1, 1)
        sprite('bn032_07', 3)
        sprite('bn032_08', 3)
        sprite('bn032_01', 3)
        sprite('bn032_02', 3)
        CommonSE('204_runjump_normal_1')
        DashEffects(100, 1, 1)
        sprite('bn032_03', 3)
        sprite('bn032_04', 3)
        sprite('bn032_05', 3)
        sprite('bn032_06', 3)
        CommonSE('204_runjump_normal_1')
        DashEffects(100, 1, 1)
        sprite('bn032_07', 3)
        sprite('bn032_08', 3)
        loopRest()

    @State
    def EventShakeObj():
        sprite('null', 40)
        sprite('null', 8)
        ScreenShake(0, 3000)
        CommonSE('019_quake_0')
        sprite('null', 8)
        ScreenShake(0, 3000)
        sprite('null', 8)
        ScreenShake(0, 3000)
        CommonSE('019_quake_0')
        sprite('null', 8)
        ScreenShake(0, 3000)
        sprite('null', 8)
        ScreenShake(0, 3000)
        CommonSE('019_quake_0')
        sprite('null', 8)
        ScreenShake(0, 3000)
        CommonSE('019_quake_0')
        sprite('null', 8)
        ScreenShake(0, 3000)
        CommonSE('019_quake_0')
        sprite('null', 8)
        ScreenShake(0, 3000)
        CommonSE('019_quake_0')
        label(0)
        sprite('null', 8)
        ScreenShake(0, 5000)
        CommonSE('019_quake_0')
        CommonSE('019_quake_1')
        loopRest()
        gotoLabel(0)